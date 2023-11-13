from pydantic import ValidationError
import pytest

from isic_metadata.metadata import MetadataBatch, MetadataRow


def test_batch():
    MetadataBatch(items=[MetadataRow(diagnosis="melanoma"), MetadataRow(diagnosis="melanoma")])


def test_lesions_belong_to_same_patient():
    with pytest.raises(ValidationError) as excinfo:
        MetadataBatch(
            items=[
                MetadataRow(lesion_id="foo", patient_id="foopatient"),
                MetadataRow(lesion_id="foo", patient_id="barpatient"),
            ]
        )
    assert len(excinfo.value.errors()) == 1
    assert "belong to multiple patients" in excinfo.value.errors()[0]["msg"]
