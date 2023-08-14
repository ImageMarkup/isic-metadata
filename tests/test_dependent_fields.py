from typing import Any, Optional

from pydantic import ValidationError
import pytest

from isic_metadata.fields import BenignMalignantEnum
from isic_metadata.metadata import MetadataRow


def test_diagnosis_no_benign_melanoma():
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow(diagnosis="melanoma", benign_malignant="benign")
    assert len(excinfo.value.errors()) == 1
    assert excinfo.value.errors()[0]["loc"][0] == "diagnosis"


@pytest.mark.parametrize("benign_malignant", ["malignant", "indeterminate/malignant"])
def test_diagnosis_no_malignant_nevus(benign_malignant):
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow(diagnosis="nevus", benign_malignant=benign_malignant)
    assert len(excinfo.value.errors()) == 1
    assert excinfo.value.errors()[0]["loc"][0] == "diagnosis"


@pytest.mark.parametrize("diagnosis", [None, "melanoma"])
def test_nevus_type_needs_nevus_diagnosis(diagnosis):
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow(diagnosis=diagnosis, nevus_type="spitz")
    assert len(excinfo.value.errors()) == 1
    assert excinfo.value.errors()[0]["loc"][0] == "nevus_type"


@pytest.mark.parametrize("diagnosis", [None, "basal cell carcinoma"])
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
def test_melanoma_fields_require_melanoma_diagnosis(
    diagnosis: Optional[str], field_name: str, field_value: Any
):
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow(**{field_name: field_value, "diagnosis": diagnosis})
    assert len(excinfo.value.errors()) == 1
    assert excinfo.value.errors()[0]["loc"][0] == field_name

    MetadataRow(**{field_name: field_value, "diagnosis": "melanoma"})


@pytest.mark.skip("TODO: https://github.com/ImageMarkup/tracker/issues/141")
def test_diagnosis_confirm_type_requires_diagnosis():
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow(diagnosis_confirm_type="histopathology")
    assert len(excinfo.value.errors()) == 1
    assert excinfo.value.errors()[0]["loc"][0] == "diagnosis_confirm_type"

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
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow(
            benign_malignant=benign_malignant,
            diagnosis="solar lentigo",
            diagnosis_confirm_type="single image expert consensus",
        )
    assert len(excinfo.value.errors()) == 1
    assert excinfo.value.errors()[0]["loc"][0] == "diagnosis_confirm_type"

    MetadataRow(
        benign_malignant=benign_malignant,
        diagnosis="solar lentigo",
        diagnosis_confirm_type="histopathology",
    )


def test_dermoscopic_type_requires_image_type_dermoscopic():
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow(dermoscopic_type="contact polarized")
    assert len(excinfo.value.errors()) == 1
    assert excinfo.value.errors()[0]["loc"][0] == "dermoscopic_type"

    MetadataRow(dermoscopic_type="contact polarized", image_type="dermoscopic")
