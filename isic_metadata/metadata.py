from __future__ import annotations

from collections import defaultdict
from typing import Any, Literal

from annotated_types import Ge
from pydantic import (
    AfterValidator,
    BaseModel,
    BeforeValidator,
    ConfigDict,
    ValidationError,
    field_validator,
    model_validator,
)
from pydantic_core import ErrorDetails, PydanticCustomError
from typing_extensions import Annotated

from isic_metadata.fields import (
    Age,
    AnatomSiteGeneralEnum,
    BenignMalignantEnum,
    ClinSizeLongDiamMm,
    ColorTintEnum,
    DermoscopicTypeEnum,
    DiagnosisConfirmTypeEnum,
    DiagnosisEnum,
    ImageTypeEnum,
    MelClassEnum,
    MelMitoticIndexEnum,
    MelThickMm,
    MelTypeEnum,
    NevusTypeEnum,
    SkinType,
    TBPTileTypeEnum,
)

CUSTOM_MESSAGES = {
    "enum": "Unsupported value for {loc}: '{value}'.",
    "int_parsing": "Unable to parse value as an integer.",
    "bool_parsing": "Unable to parse value as a boolean.",
    "float_parsing": "Unable to parse value as a number.",
    "greater_than_equal": "Number must be greater than or equal to {ge}.",
}


def convert_errors(e: ValidationError) -> list[ErrorDetails]:
    new_errors: list[ErrorDetails] = []
    for error in e.errors():
        custom_message = CUSTOM_MESSAGES.get(error["type"])
        if custom_message:
            ctx = error.get("ctx")
            loc = {"loc": error.get("loc")[0]}
            if ctx:
                ctx.update(loc)
                ctx.update({"value": error["input"]})

            error["msg"] = custom_message.format(**ctx) if ctx else custom_message
        new_errors.append(error)
    return new_errors


def error_incompatible_fields(
    field1: str, field2: str, field1_value: str | None = None, field2_value: str | None = None
) -> PydanticCustomError:
    message = (
        "Setting {{field1}}{maybe_field1_value} is incompatible with {{field2}}"
        "{maybe_field2_value}."
    ).format(
        maybe_field1_value=" to {field1_value}" if field1_value else "",
        maybe_field2_value=" {field2_value}" if field2_value else "",
    )

    return PydanticCustomError(
        "incompatible_fields",
        message,
        {
            "field1": field1,
            "field1_value": field1_value,
            "field2": field2,
            "field2_value": field2_value,
        },
    )


def error_missing_field(
    field1: str, field2: str, field1_value: str | None = None, field2_value: str | None = None
) -> PydanticCustomError:
    message = (
        "Setting {{field1}}{maybe_field1_value} requires setting {{field2}}{maybe_field2_value}."
    ).format(
        maybe_field1_value=" to {field1_value}" if field1_value else "",
        maybe_field2_value=" to {field2_value}" if field2_value else "",
    )

    return PydanticCustomError(
        "missing_field",
        message,
        {
            "field1": field1,
            "field1_value": field1_value,
            "field2": field2,
            "field2_value": field2_value,
        },
    )


class MetadataBatch(BaseModel):
    """
    A batch of metadata rows.

    This is useful for performing checks that span across multiple rows.
    """

    items: list[MetadataRow]

    @model_validator(mode="after")
    def check_patients_lesions(self) -> "MetadataBatch":
        lesion_to_patients: dict[str, set[str]] = defaultdict(set)

        for item in self.items:
            if item.patient_id and item.lesion_id:
                lesion_to_patients[item.lesion_id].add(item.patient_id)

        bad_lesions = [
            lesion for lesion in lesion_to_patients if len(lesion_to_patients[lesion]) > 1
        ]
        if bad_lesions:
            raise PydanticCustomError(
                "one_lesion_multiple_patients",
                "One or more lesions belong to multiple patients.",
                {"examples": bad_lesions[:5]},
            )

        return self


class MetadataRow(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        # This is useful for patient/lesion id fields, which could be numeric
        coerce_numbers_to_str=True,
        # extra values should be gathered by build_extra, so there's no need to allow them here
        extra="forbid",
    )

    age: (
        Annotated[
            int, BeforeValidator(Age.handle_85plus), AfterValidator(Age.clamp_upper_bound), Ge(0)
        ]
        | None
    ) = None
    sex: Literal["male", "female"] | None = None
    anatom_site_general: AnatomSiteGeneralEnum | None = None
    benign_malignant: BenignMalignantEnum | None = None
    diagnosis: DiagnosisEnum | None = None
    diagnosis_confirm_type: DiagnosisConfirmTypeEnum | None = None
    personal_hx_mm: bool | None = None
    family_hx_mm: bool | None = None
    clin_size_long_diam_mm: (
        Annotated[float, BeforeValidator(ClinSizeLongDiamMm.parse_measurement_str)] | None
    ) = None
    skin_type: SkinType | None = None
    melanocytic: bool | None = None
    concomitant_biopsy: bool | None = None

    mel_class: MelClassEnum | None = None
    mel_mitotic_index: MelMitoticIndexEnum | None = None
    mel_thick_mm: Annotated[float, BeforeValidator(MelThickMm.parse_measurement_str)] | None = None
    mel_type: MelTypeEnum | None = None
    mel_ulcer: bool | None = None

    patient_id: str | None = None
    lesion_id: str | None = None
    acquisition_day: int | None = None

    nevus_type: NevusTypeEnum | None = None
    image_type: ImageTypeEnum | None = None
    dermoscopic_type: DermoscopicTypeEnum | None = None
    tbp_tile_type: TBPTileTypeEnum | None = None

    unstructured: dict[str, Any] = {}

    # Unused and undocumented
    marker_pen: bool | None = None
    hairy: bool | None = None
    blurry: bool | None = None
    color_tint: ColorTintEnum | None = None

    # See https://github.com/samuelcolvin/pydantic/issues/2285 for more detail
    @model_validator(mode="before")
    @classmethod
    def build_extra(cls, values: dict[str, Any]) -> dict[str, Any]:
        structured_field_names = {field for field in cls.model_fields if field != "unstructured"}

        unstructured: dict[str, Any] = {}
        for field_name in list(values):
            if field_name not in structured_field_names:
                unstructured[field_name] = values.pop(field_name)
        values["unstructured"] = unstructured
        return values

    @field_validator("*", mode="before")
    @classmethod
    def strip(cls, v: Any) -> Any:
        # str_strip_whitespace doesn't seem to work for Literal values as it does for str and enum
        if isinstance(v, str):
            v = v.strip()

        # drop empty strings as though they were never passed
        return None if v == "" else v

    @field_validator(
        "anatom_site_general",
        "benign_malignant",
        "clin_size_long_diam_mm",
        "diagnosis_confirm_type",
        "mel_mitotic_index",
        "mel_thick_mm",
        "sex",
        mode="before",
    )
    @classmethod
    def lower(cls, v: Any) -> Any:
        if isinstance(v, str):
            v = v.lower()
        return v

    @model_validator(mode="after")
    def validate_no_benign_melanoma(self) -> "MetadataRow":
        if not self.benign_malignant:
            return self

        if (self.diagnosis == "melanoma" and self.benign_malignant == "benign") or (
            self.diagnosis == "nevus"
            and self.benign_malignant
            not in [
                BenignMalignantEnum.benign,
                BenignMalignantEnum.indeterminate_benign,
                BenignMalignantEnum.indeterminate,
            ]
        ):
            raise error_incompatible_fields(
                "diagnosis",
                "benign_malignant",
                self.diagnosis.value,
                self.benign_malignant.value,
            )

        return self

    @model_validator(mode="after")
    def validate_non_nevus_diagnoses(self) -> "MetadataRow":
        if not self.nevus_type:
            return self

        if not self.diagnosis:
            raise error_missing_field("nevus_type", "diagnosis")
        elif self.diagnosis not in [
            DiagnosisEnum.nevus,
            DiagnosisEnum.nevus_spilus,
        ]:
            raise error_incompatible_fields("nevus_type", "diagnosis", field2_value=self.diagnosis)

        return self

    @model_validator(mode="after")
    def validate_melanoma_fields(self) -> "MetadataRow":
        melanoma_fields: list[str] = [
            "mel_class",
            "mel_mitotic_index",
            "mel_thick_mm",
            "mel_type",
            "mel_ulcer",
        ]

        for field in melanoma_fields:
            if not getattr(self, field):
                continue

            if not self.diagnosis:
                raise error_missing_field(field, "diagnosis", field2_value="melanoma")
            elif self.diagnosis != "melanoma":
                raise error_incompatible_fields(
                    field, "diagnosis", field2_value=self.diagnosis.value
                )

        return self

    @model_validator(mode="after")
    def validate_dermoscopic_fields(self) -> "MetadataRow":
        if not self.dermoscopic_type:
            return self

        if not self.image_type:
            raise error_missing_field("dermoscopic_type", "image_type")

        if self.image_type != ImageTypeEnum.dermoscopic:
            raise error_incompatible_fields(
                "dermoscopic_type", "image_type", field2_value="dermoscopic"
            )

        return self

    @model_validator(mode="after")
    def validate_tbp_tile_fields(self) -> "MetadataRow":
        if not self.tbp_tile_type:
            return self

        if not self.image_type:
            raise error_missing_field("tbp_tile_type", "image_type")

        if self.image_type not in [
            ImageTypeEnum.tbp_tile_close_up,
            ImageTypeEnum.tbp_tile_overview,
        ]:
            raise error_incompatible_fields(
                "tbp_tile_type", "image_type", field2_value=self.image_type.value
            )

        return self

    @model_validator(mode="after")
    def validate_concomitant_biopsy(self) -> "MetadataRow":
        if self.concomitant_biopsy and (
            not self.diagnosis_confirm_type or self.diagnosis_confirm_type != "histopathology"
        ):
            raise error_missing_field(
                "concomitant_biopsy", "diagnosis_confirm_type", field2_value="histopathology"
            )

        return self
