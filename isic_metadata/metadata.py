from __future__ import annotations

from collections import defaultdict
import functools
import math
from typing import Any, Callable

from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    ValidationError,
    WrapValidator,
    field_validator,
    model_validator,
)
from pydantic_core import PydanticCustomError
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
    Sex,
    TBPTileTypeEnum,
)


def validate_enum_message(field_name: str, v: Any, handler: Callable[[Any], Any]):
    try:
        return handler(v)
    except ValidationError:
        raise ValueError(f"Invalid {field_name} of: {v}")


def EnumErrorMessageValidator(_, field_name: str):  # noqa: N802
    return WrapValidator(functools.partial(validate_enum_message, field_name))


class MetadataBatch(BaseModel):
    """
    A batch of metadata rows.

    This is useful for performing checks that span across multiple rows.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)
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
                "One or more lesions belong to multiple patients",
                {"examples": bad_lesions},
            )

        return self


class MetadataRow(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    age: Annotated[int, BeforeValidator(Age.validate)] | None = None
    sex: Annotated[int, BeforeValidator(Sex.validate)] | None = None
    benign_malignant: Annotated[
        BenignMalignantEnum,
        EnumErrorMessageValidator(BenignMalignantEnum, "benign_malignant"),
    ] | None = None
    diagnosis: Annotated[
        DiagnosisEnum, EnumErrorMessageValidator(DiagnosisEnum, "diagnosis")
    ] | None = None
    diagnosis_confirm_type: Annotated[
        DiagnosisConfirmTypeEnum,
        EnumErrorMessageValidator(DiagnosisConfirmTypeEnum, "diagnosis_confirm_type"),
    ] | None = None
    personal_hx_mm: bool | None = None
    family_hx_mm: bool | None = None
    clin_size_long_diam_mm: Annotated[
        float, BeforeValidator(ClinSizeLongDiamMm.validate)
    ] | None = None
    melanocytic: bool | None = None
    patient_id: Annotated[str, BeforeValidator(lambda x: str(x))] | None = None
    lesion_id: Annotated[str, BeforeValidator(lambda x: str(x))] | None = None
    acquisition_day: int | None = None
    marker_pen: bool | None = None
    hairy: bool | None = None
    blurry: bool | None = None
    nevus_type: Annotated[
        NevusTypeEnum, EnumErrorMessageValidator(NevusTypeEnum, "nevus_type")
    ] | None = None
    image_type: Annotated[
        ImageTypeEnum, EnumErrorMessageValidator(ImageTypeEnum, "image_type")
    ] | None = None
    dermoscopic_type: Annotated[
        DermoscopicTypeEnum, EnumErrorMessageValidator(DermoscopicTypeEnum, "dermoscopic_type")
    ] | None = None
    tbp_tile_type: Annotated[
        TBPTileTypeEnum, EnumErrorMessageValidator(TBPTileTypeEnum, "tbp_tile_type")
    ] | None = None
    anatom_site_general: Annotated[
        AnatomSiteGeneralEnum,
        EnumErrorMessageValidator(AnatomSiteGeneralEnum, "anatom_site_general"),
    ] | None = None
    color_tint: Annotated[
        ColorTintEnum, EnumErrorMessageValidator(ColorTintEnum, "color_tint")
    ] | None = None
    mel_class: Annotated[
        MelClassEnum, EnumErrorMessageValidator(MelClassEnum, "mel_class")
    ] | None = None
    mel_mitotic_index: Annotated[
        MelMitoticIndexEnum, EnumErrorMessageValidator(MelMitoticIndexEnum, "mel_mitotic_index")
    ] | None = None
    mel_thick_mm: Annotated[float, BeforeValidator(MelThickMm.validate)] | None = None
    mel_type: Annotated[
        MelTypeEnum, EnumErrorMessageValidator(MelTypeEnum, "mel_type")
    ] | None = None
    mel_ulcer: bool | None = None

    unstructured: dict[str, Any] | None = {}

    # See https://github.com/samuelcolvin/pydantic/issues/2285 for more detail
    @model_validator(mode="before")
    @classmethod
    def build_extra(cls, values: dict[str, Any]) -> dict[str, Any]:  # noqa: N805
        structured_field_names = [field for field in cls.model_fields if field != "unstructured"]

        unstructured: dict[str, Any] = {}
        for field_name in list(values):
            if field_name not in structured_field_names:
                unstructured[field_name] = values.pop(field_name)
        values["unstructured"] = unstructured
        return values

    @field_validator("*", mode="before")
    @classmethod
    def strip(cls, v: Any) -> Any:
        if isinstance(v, str):
            v = v.strip()
        return v

    @model_validator(mode="before")
    @classmethod
    def strip_none_and_nan_values(cls, values: dict[str, Any]) -> dict[str, Any]:
        for field_name, value in list(values.items()):
            if value is None or (isinstance(value, float) and math.isnan(value)):
                del values[field_name]
            elif isinstance(value, str) and not value.strip():
                del values[field_name]
        return values

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
        if self.benign_malignant is not None:
            if self.diagnosis == "melanoma" and self.benign_malignant == "benign":
                raise ValueError("A benign melanoma cannot exist.")

            if self.diagnosis == "nevus" and self.benign_malignant not in [
                BenignMalignantEnum.benign,
                BenignMalignantEnum.indeterminate_benign,
                BenignMalignantEnum.indeterminate,
            ]:
                raise ValueError(f"A {self.benign_malignant} nevus cannot exist.")

        return self

    @model_validator(mode="after")
    def validate_non_nevus_diagnoses(self) -> "MetadataRow":
        if self.diagnosis is None:
            raise ValueError("Nevus type requires a diagnosis.")

        if self.nevus_type is not None and self.diagnosis not in [
            DiagnosisEnum.nevus,
            DiagnosisEnum.nevus_spilus,
        ]:
            raise ValueError(f"Nevus type is inconsistent with {self.diagnosis}.")

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
            if self.diagnosis is None:
                raise ValueError(f"{field} requires a diagnosis of melanoma.")

            if getattr(self, field) is not None and self.diagnosis and self.diagnosis != "melanoma":
                raise ValueError(f"A non-melanoma {self.diagnosis} cannot exist.")

        return self

    @model_validator(mode="after")
    def validate_dermoscopic_fields(self) -> "MetadataRow":
        if self.image_type is None and self.dermoscopic_type is not None:
            raise ValueError(f"Dermoscopic type {self.dermoscopic_type} requires an image type.")

        if self.image_type != ImageTypeEnum.dermoscopic and self.dermoscopic_type is not None:
            raise ValueError(
                f"Image type {self.image_type} inconsistent with dermoscopic type '{self.dermoscopic_type}'."
            )

        return self

    @model_validator(mode="after")
    def validate_tbp_tile_fields(self) -> "MetadataRow":
        if self.image_type is None and self.tbp_tile_type is not None:
            raise ValueError(f"TBP tile type {self.tbp_tile_type} requires an image type.")

        if (
            self.image_type
            not in [ImageTypeEnum.tbp_tile_close_up, ImageTypeEnum.tbp_tile_overview]
            and self.tbp_tile_type is not None
        ):
            raise ValueError(
                f"Image type {self.image_type} inconsistent with TBP tile type '{self.tbp_tile_type}'."
            )

        return self
