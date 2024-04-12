from typing import Any

from hypothesis import given
from hypothesis import strategies as st
from pydantic import ValidationError
import pytest

from isic_metadata.metadata import MetadataRow, convert_errors


@pytest.mark.parametrize(
    ("field", "str_value", "parsed_value", "dependent_fields"),
    # dependent_fields is a dict of field names to values are there just to satisfy
    # the field validators.
    [
        ("age", "54", 54, {}),
        ("melanocytic", "True", True, {}),
        ("clin_size_long_diam_mm", "4mm", 4.0, {}),
        ("mel_thick_mm", ".33mm", 0.33, {"diagnosis": "melanoma"}),
        ("mel_ulcer", "false", False, {"diagnosis": "melanoma"}),
        ("family_hx_mm", "False", False, {}),
        ("personal_hx_mm", "0", False, {}),
        ("acquisition_day", "142", 142, {}),
    ],
)
def test_non_str_types(
    field: str, str_value: str, parsed_value: Any, dependent_fields: dict[str, Any]
):
    as_str = MetadataRow.model_validate({field: str_value, **dependent_fields})
    as_real = MetadataRow.model_validate({field: parsed_value, **dependent_fields})

    assert as_str.model_dump()[field] == as_real.model_dump()[field]


@pytest.mark.parametrize(("emptyish_value"), ["", " ", "\t", None])
def test_empty_fields_are_omitted(emptyish_value: Any):
    metadata = MetadataRow.model_validate({"diagnosis": "melanoma", "mel_type": emptyish_value})
    assert metadata.diagnosis == "melanoma"
    assert metadata.mel_thick_mm is None


def test_unstructured_fields():
    metadata = MetadataRow.model_validate({"diagnosis": "melanoma", "hello": "world"})
    assert metadata.diagnosis == "melanoma"
    assert metadata.unstructured["hello"] == "world"


def test_melanoma_fields():
    with pytest.raises(ValidationError) as excinfo:
        # mel_class can only be set if diagnosis is melanoma
        MetadataRow.model_validate({"diagnosis": "angioma", "mel_class": "invasive melanoma"})
    assert len(excinfo.value.errors()) == 1
    assert "mel_class is incompatible with diagnosis" in excinfo.value.errors()[0]["msg"]

    # mel_class can only be set if diagnosis is melanoma
    MetadataRow.model_validate({"diagnosis": "melanoma", "mel_class": "invasive melanoma"})


@given(age=st.integers(min_value=0).map(str))
def test_age_ceiling(age: str):
    metadata = MetadataRow.model_validate({"age": age})
    assert metadata.age is not None
    assert metadata.age <= 85


def test_age_special_case():
    assert MetadataRow.model_validate({"age": "85+"}).age == 85


def test_fitzpatrick_skin_type():
    MetadataRow.model_validate({"fitzpatrick_skin_type": "I"})


def test_benign_malignant():
    MetadataRow.model_validate({"benign_malignant": "benign"})


def test_nevus_diagnosis():
    MetadataRow.model_validate({"diagnosis": "nevus", "nevus_type": "blue"})


@pytest.mark.parametrize(
    ("raw", "parsed"),
    [
        ("4.5 mm", 4.5),
        ("14.2   mm", 14.2),
        ("4.5mm", 4.5),
        ("1mm", 1.0),
        ("3.25", 3.25),
    ],
)
def test_mel_thick_mm(raw: str, parsed: float):
    metadata = MetadataRow.model_validate({"diagnosis": "melanoma", "mel_thick_mm": raw})
    assert metadata.mel_thick_mm == parsed


def test_mel_thick_mm_invalid():
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow.model_validate({"mel_thick_mm": "foo"})
    assert len(excinfo.value.errors()) == 1
    assert "Unable to parse value as a number" in convert_errors(excinfo.value)[0]["msg"]


@given(
    clin_size=st.one_of(st.floats(min_value=0, exclude_min=True), st.integers(min_value=1)).map(
        lambda x: f"{x} mm"
    )
)
def test_clin_size_long_diam_mm_always_rounded(clin_size: str):
    metadata = MetadataRow.model_validate({"clin_size_long_diam_mm": clin_size})
    assert isinstance(metadata.clin_size_long_diam_mm, float)
    assert metadata.clin_size_long_diam_mm == round(metadata.clin_size_long_diam_mm, ndigits=1)


def test_clin_size_long_diam_mm_invalid():
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow.model_validate({"clin_size_long_diam_mm": "foo"})
    assert len(excinfo.value.errors()) == 1
    assert "Unable to parse value as a number" in convert_errors(excinfo.value)[0]["msg"]
