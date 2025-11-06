from pydantic_to_pyarrow import get_pyarrow_schema

from isic_metadata.metadata import MetadataRow
from isic_metadata.utils import get_unstructured_columns


def test_get_unstructured_columns():
    assert get_unstructured_columns(["age", "foo", "bar"]) == ["bar", "foo"]


def test_get_unstructured_columns_ignore_filename():
    assert get_unstructured_columns(["age", "foo", "bar", "filename"]) == ["bar", "foo"]


def test_pyarrow_schema():
    get_pyarrow_schema(MetadataRow, exclude_fields=True)
