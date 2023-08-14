from typing import Any

from hypothesis import given, strategies as st
from pydantic import ValidationError
import pytest

from isic_metadata.metadata import MetadataRow


def test_unstructured_fields():
    metadata = MetadataRow(diagnosis="melanoma", hello="world")
    assert metadata.diagnosis == "melanoma"
    assert metadata.unstructured["hello"] == "world"


def test_melanoma_fields():
    try:
        # mel_class can only be set if diagnosis is melanoma
        MetadataRow(diagnosis="angioma", mel_class="invasive melanoma")
    except ValidationError as e:
        assert len(e.errors()) == 1
        assert e.errors()[0]["loc"][0] == "mel_class"

    # mel_class can only be set if diagnosis is melanoma
    MetadataRow(diagnosis="melanoma", mel_class="invasive melanoma")


def test_no_benign_melanoma():
    try:
        MetadataRow(diagnosis="melanoma", benign_malignant="benign")
    except ValidationError as e:
        assert len(e.errors()) == 1
        assert e.errors()[0]["loc"][0] == "diagnosis"


@given(age=st.integers(min_value=0).map(str))
def test_age_ceiling(age):
    assert MetadataRow(age=age).age <= 85


def test_age_special_case():
    assert MetadataRow(age="85+").age == 85


@given(
    clin_size=st.one_of(st.floats(min_value=0, exclude_min=True), st.integers(min_value=1)).map(
        lambda x: f"{x} mm"
    )
)
def test_clin_size_long_diam_mm_always_rounded(clin_size):
    metadata = MetadataRow(clin_size_long_diam_mm=clin_size)
    assert isinstance(metadata.clin_size_long_diam_mm, float)
    assert metadata.clin_size_long_diam_mm == round(metadata.clin_size_long_diam_mm, ndigits=1)


@pytest.mark.parametrize(
    "field, str_value, parsed_value",
    [
        ["age", "54", 54],
        ["melanocytic", "True", True],
        ["clin_size_long_diam_mm", "4mm", 4.0],
        ["mel_thick_mm", ".33mm", 0.33],
        ["mel_ulcer", "false", False],
        ["family_hx_mm", "False", False],
        ["personal_hx_mm", "0", False],
        ["acquisition_day", "142", 142],
    ],
)
def test_non_str_types(field: str, str_value: str, parsed_value: Any):
    as_str = MetadataRow(**{field: str_value})
    as_real = MetadataRow(**{field: parsed_value})

    assert as_str.dict()[field] == as_real.dict()[field]
