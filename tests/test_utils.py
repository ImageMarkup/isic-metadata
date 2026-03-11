from __future__ import annotations

from pydantic_to_pyarrow import get_pyarrow_schema

from isic_metadata.metadata import MetadataRow
from isic_metadata.utils import get_unstructured_columns


def test_get_unstructured_columns() -> None:
    assert get_unstructured_columns(["age", "foo", "bar"]) == ["bar", "foo"]


def test_get_unstructured_columns_ignore_filename() -> None:
    assert get_unstructured_columns(["age", "foo", "bar", "filename"]) == ["bar", "foo"]


def test_pyarrow_schema() -> None:
    get_pyarrow_schema(MetadataRow, exclude_fields=True)
