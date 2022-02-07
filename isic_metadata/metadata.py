from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, root_validator, validator

from isic_metadata.fields import (
    Age,
    AnatomSiteGeneral,
    BenignMalignant,
    BenignMalignantEnum,
    ClinSizeLongDiamMm,
    ColorTint,
    DermoscopicType,
    Diagnosis,
    DiagnosisConfirmType,
    DiagnosisEnum,
    ImageType,
    ImageTypeEnum,
    LesionId,
    MelClass,
    MelMitoticIndex,
    MelThickMm,
    MelType,
    NevusType,
    PatientId,
    Sex,
)


class MetadataRow(BaseModel):
    age: Optional[Age]
    sex: Optional[Sex]
    benign_malignant: Optional[BenignMalignant]
    diagnosis: Optional[Diagnosis]
    diagnosis_confirm_type: Optional[DiagnosisConfirmType]
    personal_hx_mm: Optional[bool]
    family_hx_mm: Optional[bool]
    clin_size_long_diam_mm: Optional[ClinSizeLongDiamMm]
    melanocytic: Optional[bool]
    patient_id: Optional[PatientId]
    lesion_id: Optional[LesionId]
    acquisition_day: Optional[int]
    marker_pen: Optional[bool]
    hairy: Optional[bool]
    blurry: Optional[bool]
    nevus_type: Optional[NevusType]
    image_type: Optional[ImageType]
    dermoscopic_type: Optional[DermoscopicType]
    anatom_site_general: Optional[AnatomSiteGeneral]
    color_tint: Optional[ColorTint]
    mel_class: Optional[MelClass]
    mel_mitotic_index: Optional[MelMitoticIndex]
    mel_thick_mm: Optional[MelThickMm]
    mel_type: Optional[MelType]
    mel_ulcer: Optional[bool]

    unstructured: Optional[dict]

    # See https://github.com/samuelcolvin/pydantic/issues/2285 for more detail
    @root_validator(pre=True)
    def build_extra(cls, values: dict[str, Any]) -> dict[str, Any]:  # noqa: N805
        all_required_field_names = {
            field.alias for field in cls.__fields__.values() if field.alias != 'unstructured'
        }  # to support alias

        unstructured: dict[str, Any] = {}
        for field_name in list(values):
            if field_name not in all_required_field_names:
                unstructured[field_name] = values.pop(field_name)
        values['unstructured'] = unstructured
        return values

    @validator('*', pre=True)
    @classmethod
    def strip(cls, v):
        if isinstance(v, str):
            v = v.strip()
        return v

    @validator(
        'anatom_site_general',
        'benign_malignant',
        'clin_size_long_diam_mm',
        'diagnosis_confirm_type',
        'mel_mitotic_index',
        'mel_thick_mm',
        'sex',
        pre=True,
    )
    @classmethod
    def lower(cls, v):
        if isinstance(v, str):
            v = v.lower()
        return v

    @validator('diagnosis')
    @classmethod
    def validate_no_benign_melanoma(cls, v, values):
        if 'benign_malignant' in values:

            if v == 'melanoma' and values['benign_malignant'] == 'benign':
                raise ValueError('A benign melanoma cannot exist.')

            if v == 'nevus' and values['benign_malignant'] not in [
                BenignMalignantEnum.benign,
                BenignMalignantEnum.indeterminate_benign,
                BenignMalignantEnum.indeterminate,
            ]:
                raise ValueError(f'A {values["benign_malignant"]} nevus cannot exist.')

        return v

    @validator('nevus_type')
    @classmethod
    def validate_non_nevus_diagnoses(cls, v, values):
        if (
            v
            and values.get('diagnosis')
            and values['diagnosis'] not in [DiagnosisEnum.nevus, DiagnosisEnum.nevus_spilus]
        ):
            raise ValueError(f'Nevus type is inconsistent with {values["diagnosis"]}.')
        return v

    @validator('mel_class', 'mel_mitotic_index', 'mel_thick_mm', 'mel_type', 'mel_ulcer')
    @classmethod
    def validate_melanoma_fields(cls, v, values, config, field):
        if v and 'diagnosis' in values and values['diagnosis'] != 'melanoma':
            raise ValueError(f'A non-melanoma {field} cannot exist.')
        return v

    @validator('diagnosis_confirm_type')
    @classmethod
    def validate_non_histopathology_diagnoses(cls, v, values):
        if 'diagnosis' not in values:
            raise ValueError('Diagnosis confirm type requires a diagnosis.')

        if 'benign_malignant' in values:
            if v != 'histopathology' and values['benign_malignant'] in [
                BenignMalignantEnum.malignant,
                BenignMalignantEnum.indeterminate_benign,
                BenignMalignantEnum.indeterminate_malignant,
                BenignMalignantEnum.indeterminate,
            ]:

                raise ValueError(f'A {values["benign_malignant"]} ...')

        return v

    @validator('dermoscopic_type')
    @classmethod
    def validate_dermoscopic_fields(cls, v, values):
        if values.get('image_type') != ImageTypeEnum.dermoscopic and v:
            image_type = values.get('image_type', 'none')
            raise ValueError(f'Image type {image_type} inconsistent with dermoscopic type {v}.')
        return v
