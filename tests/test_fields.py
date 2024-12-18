from decimal import Decimal
from typing import Any

from hypothesis import given
from hypothesis import strategies as st
from pydantic import ValidationError
import pytest

from isic_metadata.diagnosis_hierarchical import DiagnosisEnum
from isic_metadata.fields import AnatomSiteGeneralEnum
from isic_metadata.metadata import MetadataRow, convert_errors


@pytest.mark.parametrize(
    ("field", "str_value", "parsed_value", "dependent_fields"),
    # dependent_fields is a dict of field names to values are there just to satisfy
    # the field validators.
    [
        ("age", "54", 54, {}),
        ("melanocytic", "True", True, {}),
        ("clin_size_long_diam_mm", "4mm", Decimal("4.0"), {}),
        ("mel_thick_mm", ".33mm", Decimal("0.33"), {"diagnosis": "Melanoma Invasive"}),
        ("mel_ulcer", "false", False, {"diagnosis": "Melanoma Invasive"}),
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
    metadata = MetadataRow.model_validate({"diagnosis": "Benign", "mel_ulcer": emptyish_value})
    assert metadata.diagnosis == "Benign"
    assert metadata.mel_thick_mm is None


def test_unstructured_fields():
    metadata = MetadataRow.model_validate({"diagnosis": "Benign", "hello": "world"})
    assert metadata.diagnosis == "Benign"
    assert metadata.unstructured["hello"] == "world"


@pytest.mark.parametrize(("melanoma_diagnosis"), DiagnosisEnum._melanoma_diagnoses())
def test_melanoma_fields(melanoma_diagnosis: str):
    with pytest.raises(ValidationError) as excinfo:
        # mel_ulcer can only be set if diagnosis is melanoma
        MetadataRow.model_validate({"diagnosis": "Benign", "mel_ulcer": True})
    assert len(excinfo.value.errors()) == 1
    assert "mel_ulcer is incompatible with diagnosis" in excinfo.value.errors()[0]["msg"]

    # mel_ulcer can only be set if diagnosis is melanoma
    MetadataRow.model_validate({"diagnosis": melanoma_diagnosis, "mel_ulcer": True})


@given(age=st.integers(min_value=0).map(str))
def test_age_ceiling(age: str):
    metadata = MetadataRow.model_validate({"age": age})
    assert metadata.age is not None
    assert metadata.age <= 85


def test_age_special_case():
    assert MetadataRow.model_validate({"age": "85+"}).age == 85


def test_fitzpatrick_skin_type():
    MetadataRow.model_validate({"fitzpatrick_skin_type": "I"})


@pytest.mark.parametrize(
    ("raw", "parsed"),
    [
        ("4.5 mm", Decimal("4.5")),
        ("14.2   mm", Decimal("14.2")),
        ("4.5mm", Decimal("4.5")),
        ("1mm", Decimal("1.0")),
        ("3.25", Decimal("3.25")),
    ],
)
def test_mel_thick_mm(raw: str, parsed: float):
    metadata = MetadataRow.model_validate({"diagnosis": "Melanoma Invasive", "mel_thick_mm": raw})
    assert metadata.mel_thick_mm == parsed


def test_mel_thick_mm_invalid():
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow.model_validate({"mel_thick_mm": "foo"})
    assert len(excinfo.value.errors()) == 1
    assert "Unable to parse value as a number" in convert_errors(excinfo.value)[0]["msg"]


@given(
    clin_size=st.one_of(
        # keep max values bounded so they don't generate larger than representable decimals.
        # disallow infinity to avoid the string 'inf'.
        st.floats(min_value=0, max_value=1_000_000, exclude_min=True, allow_infinity=False),
        st.integers(min_value=1, max_value=1_000),
    ).map(lambda x: f"{x} mm")
)
def test_clin_size_long_diam_mm_always_rounded(clin_size: str):
    metadata = MetadataRow.model_validate({"clin_size_long_diam_mm": clin_size})
    assert isinstance(metadata.clin_size_long_diam_mm, Decimal)
    assert metadata.clin_size_long_diam_mm == round(metadata.clin_size_long_diam_mm, ndigits=1)


def test_clin_size_long_diam_mm_invalid():
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow.model_validate({"clin_size_long_diam_mm": "foo"})
    assert len(excinfo.value.errors()) == 1
    assert "Unable to parse value as a number" in convert_errors(excinfo.value)[0]["msg"]


@pytest.mark.parametrize(
    ("anatom_site_special", "anatom_site_general_values"),
    [
        ("acral NOS", ["upper extremity", "lower extremity", "palms/soles"]),
        ("nail NOS", ["upper extremity", "lower extremity", "palms/soles"]),
        ("fingernail", ["upper extremity", "palms/soles"]),
        ("toenail", ["lower extremity", "palms/soles"]),
        ("acral palms or soles", ["upper extremity", "lower extremity", "palms/soles"]),
        (
            "oral or genital",
            ["head/neck", "oral/genital", "lower extremity", "anterior torso", "posterior torso"],
        ),
    ],
)
def test_anatom_site_special(anatom_site_special: str, anatom_site_general_values: list[str]):
    for anatom_site_general_value in anatom_site_general_values:
        metadata = MetadataRow.model_validate(
            {
                "anatom_site_special": anatom_site_special,
                "anatom_site_general": anatom_site_general_value,
            }
        )
        assert metadata.anatom_site_special == anatom_site_special
        assert metadata.anatom_site_general == anatom_site_general_value

    for invalid_anatom_site_general in AnatomSiteGeneralEnum:
        if invalid_anatom_site_general.value not in anatom_site_general_values:
            with pytest.raises(ValidationError) as excinfo:
                MetadataRow.model_validate(
                    {
                        "anatom_site_special": anatom_site_special,
                        "anatom_site_general": invalid_anatom_site_general.value,
                    }
                )
            assert len(excinfo.value.errors()) == 1
            assert "is incompatible with anatom_site_general" in excinfo.value.errors()[0]["msg"]


def test_anatom_site_special_requires_anatom_site_general():
    with pytest.raises(ValidationError) as excinfo:
        MetadataRow.model_validate({"anatom_site_special": "acral NOS"})
    assert len(excinfo.value.errors()) == 1
    assert "requires setting anatom_site_general" in excinfo.value.errors()[0]["msg"]
