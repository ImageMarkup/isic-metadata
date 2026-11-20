from __future__ import annotations

from enum import StrEnum
import inspect
from typing import Any

from hypothesis import given
from hypothesis import strategies as st
from pydantic import ValidationError, computed_field
import pytest

from isic_metadata import FORBIDDEN_LEADING_CHARS, MetadataRow, fields
from isic_metadata.anatom_site_hierarchical import AnatomSiteEnum
from isic_metadata.diagnosis_hierarchical import DiagnosisEnum


def _assert_rejected(model: type[MetadataRow], row: dict[str, Any], field: str) -> None:
    with pytest.raises(ValidationError) as excinfo:
        model.model_validate(row)

    errors = excinfo.value.errors()
    assert len(errors) == 1
    assert errors[0]["type"] == "forbidden_leading_character"
    assert f"Setting {field} to a value starting with" in errors[0]["msg"]


def test_enum_values_never_need_escaping() -> None:
    enums = [
        member
        for _, member in inspect.getmembers(fields, inspect.isclass)
        if issubclass(member, StrEnum) and member is not StrEnum
    ]
    assert enums

    for enum in enums:
        for member in enum:
            assert not member.value.startswith(FORBIDDEN_LEADING_CHARS)

    # the exported values of a hierarchy are its individual levels
    for hierarchy in [AnatomSiteEnum, DiagnosisEnum]:
        for member in hierarchy:
            for level in member.value.split(":"):
                assert not level.startswith(FORBIDDEN_LEADING_CHARS)


@given(
    char=st.sampled_from(FORBIDDEN_LEADING_CHARS),
    rest=st.text(),
    leading_whitespace=st.sampled_from(["", " ", "\t", "\r\n"]),
)
def test_text_values_needing_escaping_are_rejected(
    char: str, rest: str, leading_whitespace: str
) -> None:
    value = f"{leading_whitespace}{char}{rest}"

    # these are the only fields a contributor supplies as free text. every other field is an enum,
    # a literal, a boolean, or a number.
    _assert_rejected(MetadataRow, {"patient_id": value}, "patient_id")
    _assert_rejected(MetadataRow, {"lesion_id": value}, "lesion_id")
    _assert_rejected(MetadataRow, {"rcm_case_id": value, "image_type": "RCM: tile"}, "rcm_case_id")


def test_values_are_judged_by_how_they_are_exported() -> None:
    # ids are coerced to strings, so a numeric id becomes the text "-5" and is rejected like any
    # other text
    _assert_rejected(MetadataRow, {"patient_id": -5}, "patient_id")

    row = MetadataRow.model_validate(
        {
            "patient_id": "P-1",
            "lesion_id": 12345,
            "rcm_case_id": "R+1",
            "image_type": "RCM: tile",
            "acquisition_day": -3,
            "diagnosis": "Benign - Other",
        }
    )
    # a negative number is exported as a number, and a forbidden character that isn't leading is
    # harmless. accepted values are exported untouched: the check rejects, it never escapes.
    assert row.acquisition_day == -3
    assert row.patient_id == "P-1"
    assert row.lesion_id == "12345"
    assert row.rcm_case_id == "R+1"
    assert row.diagnosis_2 == "Benign - Other"


def test_fields_added_later_cannot_bypass_the_check() -> None:
    class ExtendedRow(MetadataRow):
        note: str | None = None

        @computed_field  # type: ignore[prop-decorator]
        @property
        def derived(self) -> str | None:
            return f"@{self.lesion_id}" if self.lesion_id else None

    _assert_rejected(ExtendedRow, {"note": "=1+1"}, "note")
    # a computed field built from a clean value still can't export something needing escaping
    _assert_rejected(ExtendedRow, {"lesion_id": "L1"}, "derived")

    assert ExtendedRow.model_validate({"note": "fine"}).note == "fine"
