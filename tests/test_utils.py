import pandas as pd

from isic_metadata.utils import get_unstructured_columns


def test_get_unstructured_columns():
    data = [{'age': 25, 'foo': 'bar'}, {'age': 25}, {'age': 25, 'foo': 'bar'}]

    df = pd.DataFrame.from_records(data)

    assert get_unstructured_columns(df) == ['foo']


def test_get_unstructured_columns_ignore_filename():
    data = [{'age': 25, 'foo': 'bar', 'filename': 'foobar'}, {'age': 25}, {'age': 25, 'foo': 'bar'}]

    df = pd.DataFrame.from_records(data)

    assert get_unstructured_columns(df) == ['foo']
