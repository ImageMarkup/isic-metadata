from pydantic import ValidationError
import pytest

from isic_metadata.diagnosis_hierarchical import DiagnosisEnum
from isic_metadata.metadata import MetadataRow


@pytest.mark.parametrize(
    ("raw", "parsed"),
    [
        ("Benign", ["Benign"]),
        ("Benign - Other", ["Benign", "Benign - Other"]),
        ("Blue nevus", ["Benign", "Benign melanocytic proliferations", "Nevus", "Blue nevus"]),
        (
            "Squamous cell carcinoma, NOS",
            ["Malignant", "Malignant epidermal proliferations", "Squamous cell carcinoma, NOS"],
        ),
        (
            "Blue nevus, Sclerosing",
            [
                "Benign",
                "Benign melanocytic proliferations",
                "Nevus",
                "Blue nevus",
                "Blue nevus, Sclerosing",
            ],
        ),
    ],
)
def test_diagnosis(raw, parsed):
    metadata = MetadataRow.model_validate({"diagnosis": raw})

    for i, diagnosis in enumerate(parsed, start=1):
        assert getattr(metadata, f"diagnosis_{i}") == diagnosis


def test_top_level_diagnosis_is_never_exported():
    metadata = MetadataRow.model_validate({"diagnosis": "Benign"})
    assert "diagnosis" not in metadata.model_dump()
    assert metadata.diagnosis_1 == "Benign"


def test_diagnosis_enum_has_unique_terminal_values():
    terminal_nodes = [member.value.split(":")[-1] for member in DiagnosisEnum]
    assert len(terminal_nodes) == len(set(terminal_nodes))


def test_single_value_diagnosis_is_favored():
    # test that passing in a single diagnosis value is favored over multiple values. used
    # for when data is coming from the database and potentially contains an existing
    # 1..5 diagnosis and a newly updated single diagnosis.
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow.model_validate(
            {
                "diagnosis": "Fibroma, Sclerotic",
                "mel_ulcer": True,
                # these should be ignored
                "diagnosis_1": "Benign",
                "diagnosis_2": "Benign melanocytic proliferations",
                "diagnosis_3": "Nevus",
            }
        )
    assert "Setting mel_ulcer is incompatible with diagnosis" in excinfo.value.errors()[0]["msg"]


def test_diagnosis_multiple_levels_is_coerced():
    # test that passing in diagnosis_1..5 is coerced into a single diagnosis field to handle
    # cross field input validation
    metadata = MetadataRow.model_validate({"diagnosis_1": "Benign"})
    assert metadata.diagnosis_1 == "Benign"
    assert metadata.diagnosis_2 is None
    assert metadata.diagnosis_3 is None
    assert metadata.diagnosis_4 is None
    assert metadata.diagnosis_5 is None


def test_diagnosis_validation_is_idempotent():
    # test that running model_validate on a MetadataRow multiple times does not change the
    # output
    metadata = MetadataRow.model_validate({"diagnosis": "Melanoma Invasive"})
    assert metadata.diagnosis_1 == "Malignant"
    assert metadata.diagnosis_2 == "Malignant melanocytic proliferations (Melanoma)"
    assert metadata.diagnosis_3 == "Melanoma Invasive"
    metadata_2 = MetadataRow.model_validate(
        metadata.model_dump(exclude_unset=True, exclude_none=True, exclude={"unstructured"})
    )
    assert metadata == metadata_2
