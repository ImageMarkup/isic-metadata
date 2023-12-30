from isic_metadata.utils import get_unstructured_columns


def test_get_unstructured_columns():
    assert get_unstructured_columns(["age", "foo", "bar"]) == ["bar", "foo"]


def test_get_unstructured_columns_ignore_filename():
    assert get_unstructured_columns(["age", "foo", "bar", "filename"]) == ["bar", "foo"]
