from pydantic import ValidationError
import pytest

from isic_metadata.metadata import MetadataBatch, MetadataRow


def test_batch():
    MetadataBatch(
        items=[
            MetadataRow.model_validate({"sex": "male"}),
            MetadataRow.model_validate({"sex": "male"}),
        ]
    )


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


def test_blank_lesions_dont_belong_to_same_patient():
    MetadataBatch(
        items=[
            MetadataRow(lesion_id="", patient_id="foopatient"),
            MetadataRow(lesion_id="", patient_id="barpatient"),
        ]
    )


def test_rcm_case_has_at_most_one_macroscopic_image():
    with pytest.raises(ValidationError) as excinfo:
        MetadataBatch(
            items=[
                MetadataRow(image_type="RCM: macroscopic", rcm_case_id="foo"),
                MetadataRow(image_type="RCM: macroscopic", rcm_case_id="foo"),
            ]
        )
    assert len(excinfo.value.errors()) == 1
    assert "have multiple macroscopic images" in excinfo.value.errors()[0]["msg"]

    MetadataBatch(
        items=[
            MetadataRow(image_type="RCM: macroscopic", rcm_case_id="foo"),
            MetadataRow(image_type="RCM: macroscopic", rcm_case_id="bar"),
        ]
    )


def test_rcm_cases_belong_to_same_lesion():
    with pytest.raises(ValidationError) as excinfo:
        MetadataBatch(
            items=[
                MetadataRow(
                    rcm_case_id="foo", lesion_id="foolesion", _ignore_rcm_model_checks=True
                ),
                MetadataRow(
                    rcm_case_id="foo", lesion_id="barlesion", _ignore_rcm_model_checks=True
                ),
            ]
        )
    assert len(excinfo.value.errors()) == 1
    assert "belong to multiple lesions" in excinfo.value.errors()[0]["msg"]


def test_blank_rcm_cases_dont_belong_to_same_lesion():
    MetadataBatch(
        items=[
            MetadataRow(rcm_case_id="", lesion_id="foolesion"),
            MetadataRow(rcm_case_id="", lesion_id="barlesion"),
        ]
    )
