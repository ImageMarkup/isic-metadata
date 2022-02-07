from hypothesis import given, strategies as st
from pydantic import ValidationError

from isic_metadata.metadata import MetadataRow


def test_melanoma_fields():
    try:
        # mel_class can only be set if diagnosis is melanoma
        MetadataRow(diagnosis='angioma', mel_class='invasive melanoma')
    except ValidationError as e:
        assert len(e.errors()) == 1
        assert e.errors()[0]['loc'][0] == 'mel_class'

    # mel_class can only be set if diagnosis is melanoma
    MetadataRow(diagnosis='melanoma', mel_class='invasive melanoma')


def test_no_benign_melanoma():
    try:
        MetadataRow(diagnosis='melanoma', benign_malignant='benign')
    except ValidationError as e:
        assert len(e.errors()) == 1
        assert e.errors()[0]['loc'][0] == 'diagnosis'


@given(age=st.integers(min_value=0).map(str))
def test_age_ceiling(age):
    assert MetadataRow(age=age).age <= 85


def test_age_special_case():
    assert MetadataRow(age='85+').age == 85


# test that non numeric strings fail, this should capture negative values
# @given(age=st.text().filter(lambda s: not s.isnumeric() and s != ''))
# def test_age_fuzz(age):
#     print(age)
#     with pytest.raises(ValidationError) as excinfo:
#         MetadataRow(age=age)


#     assert 'foo' == excinfo.value
# except ValidationError as e:
#     breakpoint()
#     assert len(e.errors()) == 1
#     assert e.errors()[0]['loc'][0] == 'age'
#     print(e.errors())
