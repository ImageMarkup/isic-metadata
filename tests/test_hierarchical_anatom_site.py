from pydantic import ValidationError
import pytest

from isic_metadata.anatom_site_hierarchical import AnatomSiteEnum
from isic_metadata.metadata import MetadataRow


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("Head and neck", ["Head and neck", None, None, None, None]),
        ("Head and neck:Head", ["Head and neck", "Head", None, None, None]),
        ("Head and neck:Head:Scalp", ["Head and neck", "Head", "Scalp", None, None]),
        (
            "Head and neck:Head:Scalp:Frontal scalp",
            ["Head and neck", "Head", "Scalp", "Frontal scalp", None],
        ),
        (
            "Head and neck:Head:Ear:Pinna:Helix of pinna",
            ["Head and neck", "Head", "Ear", "Pinna", "Helix of pinna"],
        ),
    ],
)
def test_levels_at_each_depth(value, expected):
    assert AnatomSiteEnum.levels(value) == expected


def test_accept_terminal_values_resolves_leaf():
    assert AnatomSiteEnum.accept_terminal_values("Scalp") == "Head and neck:Head:Scalp"
    assert (
        AnatomSiteEnum.accept_terminal_values("Helix of pinna")
        == "Head and neck:Head:Ear:Pinna:Helix of pinna"
    )


def test_accept_terminal_values_passes_through_qualified():
    qualified = "Head and neck:Head:Scalp"
    assert AnatomSiteEnum.accept_terminal_values(qualified) == qualified


def test_accept_terminal_values_has_unique_terminals():
    terminal_nodes = [member.value.split(":")[-1] for member in AnatomSiteEnum]
    assert len(terminal_nodes) == len(set(terminal_nodes))


@pytest.mark.parametrize(
    ("raw", "parsed"),
    [
        ("Head and neck", ["Head and neck"]),
        ("Scalp", ["Head and neck", "Head", "Scalp"]),
        (
            "Helix of pinna",
            ["Head and neck", "Head", "Ear", "Pinna", "Helix of pinna"],
        ),
        ("Anterior trunk", ["Trunk", "Anterior trunk"]),
        (
            "Breast",
            ["Trunk", "Anterior trunk", "Anterior chest", "Breast"],
        ),
    ],
)
def test_metadata_row_accepts_hierarchical_anatom_site(raw, parsed):
    metadata = MetadataRow.model_validate({"anatom_site": raw})
    for i, value in enumerate(parsed, start=1):
        assert getattr(metadata, f"anatom_site_{i}") == value


def test_top_level_anatom_site_is_never_exported():
    metadata = MetadataRow.model_validate({"anatom_site": "Head and neck"})
    dumped = metadata.model_dump()
    assert "anatom_site" not in dumped
    assert dumped["anatom_site_1"] == "Head and neck"


def test_metadata_row_reassembles_individual_levels():
    metadata = MetadataRow.model_validate(
        {
            "anatom_site_1": "Head and neck",
            "anatom_site_2": "Head",
            "anatom_site_3": "Scalp",
        }
    )
    assert metadata.anatom_site_1 == "Head and neck"
    assert metadata.anatom_site_2 == "Head"
    assert metadata.anatom_site_3 == "Scalp"
    assert metadata.anatom_site_4 is None
    assert metadata.anatom_site_5 is None


def test_single_value_anatom_site_is_favored_over_levels():
    metadata = MetadataRow.model_validate(
        {
            "anatom_site": "Lower extremity:Foot:Toes",
            "anatom_site_1": "Head and neck",
            "anatom_site_2": "Head",
        }
    )
    assert metadata.anatom_site_1 == "Lower extremity"
    assert metadata.anatom_site_2 == "Foot"
    assert metadata.anatom_site_3 == "Toes"


def test_anatom_site_validation_is_idempotent():
    metadata = MetadataRow.model_validate({"anatom_site": "Scalp"})
    metadata_2 = MetadataRow.model_validate(
        metadata.model_dump(exclude_unset=True, exclude_none=True, exclude={"unstructured"})
    )
    assert metadata == metadata_2


def test_anatom_site_general_and_special_unaffected():
    metadata = MetadataRow.model_validate(
        {
            "anatom_site_general": "head/neck",
            "anatom_site_special": "oral or genital",
        }
    )
    assert metadata.anatom_site_general.value == "head/neck"
    assert metadata.anatom_site_special.value == "oral or genital"


def test_anatom_site_general_coexists_with_hierarchical():
    metadata = MetadataRow.model_validate(
        {
            "anatom_site_general": "head/neck",
            "anatom_site": "Head and neck:Head:Scalp",
        }
    )
    assert metadata.anatom_site_general.value == "head/neck"
    assert metadata.anatom_site_1 == "Head and neck"
    assert metadata.anatom_site_3 == "Scalp"


def test_invalid_anatom_site_raises_error():
    with pytest.raises(ValidationError):
        MetadataRow.model_validate({"anatom_site": "Not a real site"})
