from typing import Any

from pydantic import ValidationError
import pytest

from isic_metadata.fields import BenignMalignantEnum
from isic_metadata.metadata import MetadataRow


def test_diagnosis_no_benign_melanoma():
    try:
        MetadataRow(diagnosis="melanoma", benign_malignant="benign")
    except ValidationError as e:
        assert len(e.errors()) == 1
        assert e.errors()[0]["loc"][0] == "diagnosis"


@pytest.mark.parametrize("benign_malignant", ["malignant", "indeterminate/malignant"])
def test_diagnosis_no_malignant_nevus(benign_malignant):
    try:
        MetadataRow(diagnosis="nevus", benign_malignant=benign_malignant)
    except ValidationError as e:
        assert len(e.errors()) == 1
        assert e.errors()[0]["loc"][0] == "diagnosis"


@pytest.mark.parametrize("diagnosis", [None, "melanoma"])
def test_nevus_type_needs_nevus_diagnosis(diagnosis):
    try:
        MetadataRow(diagnosis=diagnosis, nevus_type="spitz")
    except ValidationError as e:
        assert len(e.errors()) == 1
        assert e.errors()[0]["loc"][0] == "nevus_type"


@pytest.mark.parametrize(
    "field_name, field_value",
    [
        ["mel_class", "melanoma in situ"],
        ["mel_mitotic_index", "4/mm^2"],
        ["mel_thick_mm", "4mm"],
        ["mel_type", "nodular melanoma"],
        ["mel_ulcer", True],
    ],
)
def test_melanoma_fields_require_melanoma_diagnosis(field_name: str, field_value: Any):
    try:
        MetadataRow(**{field_name: field_value, "diagnosis": "basal cell carcinoma"})
    except ValidationError as e:
        assert len(e.errors()) == 1
        assert e.errors()[0]["loc"][0] == field_name

    MetadataRow(**{field_name: field_value, "diagnosis": "melanoma"})


def test_diagnosis_confirm_type_requires_diagnosis():
    try:
        MetadataRow(diagnosis_confirm_type="histopathology")
    except ValidationError as e:
        assert len(e.errors()) == 1
        assert e.errors()[0]["loc"][0] == "diagnosis_confirm_type"

    MetadataRow(diagnosis="melanoma", diagnosis_confirm_type="histopathology")


@pytest.mark.parametrize(
    "benign_malignant",
    [
        BenignMalignantEnum.malignant,
        BenignMalignantEnum.indeterminate_benign,
        BenignMalignantEnum.indeterminate_malignant,
        BenignMalignantEnum.indeterminate,
    ],
)
def test_diagnosis_confirm_type_must_be_histopathology(benign_malignant):
    try:
        MetadataRow(
            benign_malignant=benign_malignant,
            diagnosis="solar lentigo",
            diagnosis_confirm_type="single image expert consensus",
        )
    except ValidationError as e:
        assert len(e.errors()) == 1
        assert e.errors()[0]["loc"][0] == "diagnosis_confirm_type"

    MetadataRow(
        benign_malignant=benign_malignant,
        diagnosis="solar lentigo",
        diagnosis_confirm_type="histopathology",
    )


def test_dermoscopic_type_requires_image_type_dermoscopic():
    try:
        MetadataRow(dermoscopic_type="contact polarized")
    except ValidationError as e:
        assert len(e.errors()) == 1
        assert e.errors()[0]["loc"][0] == "dermoscopic_type"

    MetadataRow(dermoscopic_type="contact polarized", image_type="dermoscopic")
