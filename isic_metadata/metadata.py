from __future__ import annotations

import functools
from typing import Any, Callable, Optional, Union

from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    FieldValidationInfo,
    ValidationError,
    WrapValidator,
    field_validator,
    model_validator,
)
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
    LesionId,
    MelClassEnum,
    MelMitoticIndexEnum,
    MelThickMm,
    MelTypeEnum,
    NevusTypeEnum,
    PatientId,
    Sex,
)


def validate_enum_message(field_name: str, v: Any, handler: Callable[[Any], Any]):
    try:
        return handler(v)
    except ValidationError:
        raise ValueError(f"Invalid {field_name} of: {v}")


def EnumErrorMessageValidator(enum, field_name: str):  # noqa: N802
    return WrapValidator(functools.partial(validate_enum_message, field_name))


class MetadataRow(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    age: Optional[Annotated[Union[str, int], BeforeValidator(Age.validate)]] = None
    sex: Optional[Annotated[Union[str, int], BeforeValidator(Sex.validate)]] = None
    benign_malignant: Optional[
        Annotated[
            BenignMalignantEnum,
            EnumErrorMessageValidator(BenignMalignantEnum, "benign_malignant"),
        ]
    ] = None
    diagnosis: Optional[
        Annotated[DiagnosisEnum, EnumErrorMessageValidator(DiagnosisEnum, "diagnosis")]
    ] = None
    diagnosis_confirm_type: Optional[
        Annotated[
            DiagnosisConfirmTypeEnum,
            EnumErrorMessageValidator(DiagnosisConfirmTypeEnum, "diagnosis_confirm_type"),
        ]
    ] = None
    personal_hx_mm: Optional[bool] = None
    family_hx_mm: Optional[bool] = None
    clin_size_long_diam_mm: Optional[
        Annotated[Union[str, float], BeforeValidator(ClinSizeLongDiamMm.validate)]
    ] = None
    melanocytic: Optional[bool] = None
    # these can be passed as ints, floats, etc from pandas so they need to be coerced to strings
    patient_id: Optional[Annotated[PatientId, BeforeValidator(lambda x: str(x))]] = None
    lesion_id: Optional[Annotated[LesionId, BeforeValidator(lambda x: str(x))]] = None
    acquisition_day: Optional[int] = None
    marker_pen: Optional[bool] = None
    hairy: Optional[bool] = None
    blurry: Optional[bool] = None
    nevus_type: Optional[
        Annotated[NevusTypeEnum, EnumErrorMessageValidator(NevusTypeEnum, "nevus_type")]
    ] = None
    image_type: Optional[
        Annotated[ImageTypeEnum, EnumErrorMessageValidator(ImageTypeEnum, "image_type")]
    ] = None
    dermoscopic_type: Optional[
        Annotated[
            DermoscopicTypeEnum, EnumErrorMessageValidator(DermoscopicTypeEnum, "dermoscopic_type")
        ]
    ] = None
    anatom_site_general: Optional[
        Annotated[
            AnatomSiteGeneralEnum,
            EnumErrorMessageValidator(AnatomSiteGeneralEnum, "anatom_site_general"),
        ]
    ] = None
    color_tint: Optional[
        Annotated[ColorTintEnum, EnumErrorMessageValidator(ColorTintEnum, "color_tint")]
    ] = None
    mel_class: Optional[
        Annotated[MelClassEnum, EnumErrorMessageValidator(MelClassEnum, "mel_class")]
    ] = None
    mel_mitotic_index: Optional[
        Annotated[
            MelMitoticIndexEnum, EnumErrorMessageValidator(MelMitoticIndexEnum, "mel_mitotic_index")
        ]
    ] = None
    mel_thick_mm: Optional[
        Annotated[Union[str, float], BeforeValidator(MelThickMm.validate)]
    ] = None
    mel_type: Optional[
        Annotated[MelTypeEnum, EnumErrorMessageValidator(MelTypeEnum, "mel_type")]
    ] = None
    mel_ulcer: Optional[bool] = None

    unstructured: Optional[dict] = {}

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
    def strip(cls, v):
        if isinstance(v, str):
            v = v.strip()
        return v

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
    def lower(cls, v):
        if isinstance(v, str):
            v = v.lower()
        return v

    @field_validator("diagnosis")
    @classmethod
    def validate_no_benign_melanoma(cls, v, info: FieldValidationInfo):
        if info.data.get("benign_malignant"):
            if v == "melanoma" and info.data["benign_malignant"] == "benign":
                raise ValueError("A benign melanoma cannot exist.")

            if v == "nevus" and info.data["benign_malignant"] not in [
                BenignMalignantEnum.benign,
                BenignMalignantEnum.indeterminate_benign,
                BenignMalignantEnum.indeterminate,
            ]:
                raise ValueError(f'A {info.data["benign_malignant"]} nevus cannot exist.')

        return v

    @field_validator("nevus_type")
    @classmethod
    def validate_non_nevus_diagnoses(cls, v, info: FieldValidationInfo):
        if not info.data.get("diagnosis"):
            raise ValueError("Nevus type requires a diagnosis.")

        if v and info.data["diagnosis"] not in [DiagnosisEnum.nevus, DiagnosisEnum.nevus_spilus]:
            raise ValueError(f'Nevus type is inconsistent with {info.data["diagnosis"]}.')
        return v

    @field_validator("mel_class", "mel_mitotic_index", "mel_thick_mm", "mel_type", "mel_ulcer")
    @classmethod
    def validate_melanoma_fields(cls, v, info: FieldValidationInfo):
        if not info.data.get("diagnosis"):
            raise ValueError(f"{info.field_name} requires a diagnosis of melanoma.")

        if v and info.data.get("diagnosis") and info.data["diagnosis"] != "melanoma":
            raise ValueError(f"A non-melanoma {info.data['diagnosis']} cannot exist.")
        return v

    @field_validator("diagnosis_confirm_type")
    @classmethod
    def validate_non_histopathology_diagnoses(cls, v, info: FieldValidationInfo):
        # TODO: renable this after https://github.com/ImageMarkup/tracker/issues/141 is fixed.
        # if not info.data.get("diagnosis"):
        #     raise ValueError("Diagnosis confirm type requires a diagnosis.")

        if info.data.get("benign_malignant"):
            if v != "histopathology" and info.data["benign_malignant"] in [
                BenignMalignantEnum.malignant,
                BenignMalignantEnum.indeterminate_benign,
                BenignMalignantEnum.indeterminate_malignant,
                BenignMalignantEnum.indeterminate,
            ]:
                raise ValueError(
                    f'{info.data["benign_malignant"]} is incompatible with diagnosis_confirm_type: {v}'  # noqa: E501
                )

        return v

    @field_validator("dermoscopic_type")
    @classmethod
    def validate_dermoscopic_fields(cls, v, info: FieldValidationInfo):
        if info.data.get("image_type") != ImageTypeEnum.dermoscopic and v:
            image_type = info.data.get("image_type", "")
            raise ValueError(
                f"Image type {image_type or 'None'} inconsistent with dermoscopic type '{v.value}'."
            )
        return v
