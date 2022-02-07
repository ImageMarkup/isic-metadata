from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from isic_metadata.fields import (
    AcquisitionDay,
    AnatomSiteGeneral,
    BenignMalignant,
    ClinSizeLongDiamMm,
    ColorTint,
    DermoscopicType,
    Diagnosis,
    DiagnosisConfirmType,
    ImageType,
    LesionId,
    MelClass,
    MelMitoticIndex,
    MelThickMm,
    MelType,
    NevusType,
    PatientId,
    Sex,
)

try:
    __version__ = version('isic-metadata')
except PackageNotFoundError:
    # package is not installed
    pass


FIELD_REGISTRY = {}

for field in [
    'blurry',
    'hairy',
    'marker_pen',
    'personal_hx_mm',
    'family_hx_mm',
    'melanocytic',
    'mel_ulcer',
]:
    FIELD_REGISTRY[field] = {
        'validator': bool,
        'search': {
            'key': field,
            'es_property': {'type': 'boolean'},
            'es_facet': {'terms': {'field': field}},
        },
    }


for field, validator in [
    ('sex', Sex),
    ('benign_malignant', BenignMalignant),
    ('diagnosis_confirm_type', DiagnosisConfirmType),
    ('nevus_type', NevusType),
    ('image_type', ImageType),
    ('dermoscopic_type', DermoscopicType),
    ('mel_type', MelType),
    ('mel_class', MelClass),
    ('mel_mitotic_index', MelMitoticIndex),
    ('anatom_site_general', AnatomSiteGeneral),
    ('color_tint', ColorTint),
]:
    FIELD_REGISTRY[field] = {
        'validator': validator,
        'search': {
            'key': field,
            'es_property': {'type': 'keyword'},
            'es_facet': {'terms': {'field': field}},
        },
    }

FIELD_REGISTRY.update(
    {
        'clin_size_long_diam_mm': {
            'validator': ClinSizeLongDiamMm,
            'search': {
                'key': 'clin_size_long_diam_mm',
                'es_property': {'type': 'float'},
                'es_facet': {
                    'histogram': {
                        'field': 'clin_size_long_diam_mm',
                        'interval': 10,
                        'extended_bounds': {'min': 0, 'max': 100},
                    }
                },
            },
        },
        'acquisition_day': {
            'validator': AcquisitionDay,
            'search': False,
        },
        'diagnosis': {
            'validator': Diagnosis,
            'search': {
                'key': 'diagnosis',
                'es_property': {'type': 'keyword'},
                'es_facet': {'terms': {'field': 'diagnosis', 'size': 100}},
            },
        },
        'mel_thick_mm': {
            'validator': MelThickMm,
            'search': {
                'key': 'mel_thick_mm',
                'es_property': {'type': 'float'},
                'es_facet': {
                    'range': {
                        'field': 'mel_thick_mm',
                        'ranges': [
                            {'from': 0.0, 'to': 0.5},
                            {'from': 0.5, 'to': 1.0},
                            {'from': 1.0, 'to': 1.5},
                            {'from': 1.5, 'to': 2.0},
                            {'from': 2.0, 'to': 2.5},
                            {'from': 2.5, 'to': 3.0},
                            {'from': 3.0, 'to': 3.5},
                            {'from': 3.5, 'to': 4.0},
                            {'from': 4.0, 'to': 4.5},
                            {'from': 4.5, 'to': 5.0},
                            {'from': 5.0},
                        ],
                    }
                },
            },
        },
        'patient_id': {'validator': PatientId, 'search': False},
        'lesion_id': {'validator': LesionId, 'search': False},
    }
)

# age
