from typing import Any

from pydantic import ValidationError
import pytest

from isic_metadata.metadata import MetadataRow


def test_diagnosis_no_benign_melanoma():
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow.model_validate({"diagnosis": "melanoma", "benign_malignant": "benign"})
    assert len(excinfo.value.errors()) == 1
    assert "melanoma is incompatible with benign_malignant" in excinfo.value.errors()[0]["msg"]


@pytest.mark.parametrize("benign_malignant", ["malignant", "indeterminate/malignant"])
def test_diagnosis_no_malignant_nevus(benign_malignant: str):
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow.model_validate({"diagnosis": "nevus", "benign_malignant": benign_malignant})
    assert len(excinfo.value.errors()) == 1
    assert "nevus is incompatible with benign_malignant" in excinfo.value.errors()[0]["msg"]


@pytest.mark.parametrize(
    ["diagnosis", "error_message"],
    [[None, "requires setting diagnosis"], ["melanoma", "is incompatible with diagnosis"]],
)
def test_nevus_type_needs_nevus_diagnosis(diagnosis: str | None, error_message: str):
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow.model_validate({"diagnosis": diagnosis, "nevus_type": "spitz"})
    assert len(excinfo.value.errors()) == 1
    assert f"nevus_type {error_message}" in excinfo.value.errors()[0]["msg"]


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
    diagnosis: str | None, field_name: str, field_value: Any
):
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow.model_validate({field_name: field_value, "diagnosis": diagnosis})
    assert len(excinfo.value.errors()) == 1
    assert field_name in excinfo.value.errors()[0]["msg"]

    MetadataRow.model_validate({field_name: field_value, "diagnosis": "melanoma"})


@pytest.mark.skip("TODO: https://github.com/ImageMarkup/tracker/issues/141")
def test_diagnosis_confirm_type_requires_diagnosis():
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow.model_validate({"diagnosis_confirm_type": "histopathology"})
    assert len(excinfo.value.errors()) == 1
    assert excinfo.value.errors()[0]["loc"][0] == "diagnosis_confirm_type"

    MetadataRow.model_validate(
        {"diagnosis": "melanoma", "diagnosis_confirm_type": "histopathology"}
    )


def test_dermoscopic_type_requires_image_type_dermoscopic():
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow.model_validate({"dermoscopic_type": "contact polarized"})
    assert len(excinfo.value.errors()) == 1
    assert "dermoscopic_type requires setting image_type" in excinfo.value.errors()[0]["msg"]

    MetadataRow.model_validate(
        {"dermoscopic_type": "contact polarized", "image_type": "dermoscopic"}
    )


def test_dermoscopic_type_requires_dermoscopic_image_type():
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow.model_validate(
            {"dermoscopic_type": "contact polarized", "image_type": "clinical: overview"}
        )
    assert len(excinfo.value.errors()) == 1
    assert "dermoscopic_type is incompatible with image_type" in excinfo.value.errors()[0]["msg"]


def test_tbp_tile_type_requires_image_type_tbp_tile():
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow.model_validate({"tbp_tile_type": "2D"})
    assert len(excinfo.value.errors()) == 1
    assert "tbp_tile_type requires setting image_type" in excinfo.value.errors()[0]["msg"]

    MetadataRow.model_validate({"tbp_tile_type": "2D", "image_type": "TBP tile: close-up"})
    MetadataRow.model_validate({"tbp_tile_type": "2D", "image_type": "TBP tile: overview"})


def test_tbp_tile_type_requires_tbp_tile_image_type():
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow.model_validate({"tbp_tile_type": "2D", "image_type": "clinical: overview"})
    assert len(excinfo.value.errors()) == 1
    assert "tbp_tile_type is incompatible with image_type" in excinfo.value.errors()[0]["msg"]

    MetadataRow.model_validate({"tbp_tile_type": "2D", "image_type": "TBP tile: close-up"})
    MetadataRow.model_validate({"tbp_tile_type": "2D", "image_type": "TBP tile: overview"})


def test_concomitant_biopsy_requires_histopathology():
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow.model_validate(
            {"concomitant_biopsy": True, "diagnosis_confirm_type": "single image expert consensus"}
        )
    assert len(excinfo.value.errors()) == 1
    assert (
        "concomitant_biopsy requires setting diagnosis_confirm_type"
        in excinfo.value.errors()[0]["msg"]
    )

    MetadataRow.model_validate(
        {"concomitant_biopsy": True, "diagnosis_confirm_type": "histopathology"}
    )
    MetadataRow.model_validate(
        {"concomitant_biopsy": False, "diagnosis_confirm_type": "single image expert consensus"}
    )
