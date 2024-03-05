from __future__ import annotations

from dataclasses import dataclass
from importlib.metadata import PackageNotFoundError, version
from typing import Any, Literal

try:
    __version__ = version("isic-metadata")
except PackageNotFoundError:
    # package is not installed
    pass


@dataclass()
class SearchConfig:
    key: str
    es_property: dict[str, Any]
    es_facet: dict[str, Any]


@dataclass()
class Field:
    search: SearchConfig | None = None
    label: str | None = None
    type: Literal["acquisition", "clinical"] | None = None


FIELD_REGISTRY: dict[str, Field] = {}

for field in [
    "blurry",
    "hairy",
    "marker_pen",
    "personal_hx_mm",
    "family_hx_mm",
    "melanocytic",
    "mel_ulcer",
    "concomitant_biopsy",
]:
    FIELD_REGISTRY[field] = Field(
        search=SearchConfig(
            key=field,
            es_property={"type": "boolean"},
            es_facet={"terms": {"field": field}},
        )
    )


for field in [
    "sex",
    "benign_malignant",
    "diagnosis_confirm_type",
    "nevus_type",
    "image_type",
    "dermoscopic_type",
    "tbp_tile_type",
    "mel_type",
    "mel_class",
    "mel_mitotic_index",
    "anatom_site_general",
    "color_tint",
    "patient_id",
    "lesion_id",
    "fitzpatrick_skin_type",
]:
    FIELD_REGISTRY[field] = Field(
        search=SearchConfig(
            key=field, es_property={"type": "keyword"}, es_facet={"terms": {"field": field}}
        )
    )


FIELD_REGISTRY.update(
    {
        "clin_size_long_diam_mm": Field(
            search=SearchConfig(
                key="clin_size_long_diam_mm",
                es_property={"type": "float"},
                es_facet={
                    "histogram": {
                        "field": "clin_size_long_diam_mm",
                        "interval": 10,
                        "extended_bounds": {"min": 0, "max": 100},
                    }
                },
            )
        ),
        "acquisition_day": Field(),
        "diagnosis": Field(
            search=SearchConfig(
                key="diagnosis",
                es_property={"type": "keyword"},
                es_facet={"terms": {"field": "diagnosis", "size": 100}},
            )
        ),
        "mel_thick_mm": Field(
            search=SearchConfig(
                key="mel_thick_mm",
                es_property={"type": "float"},
                es_facet={
                    "range": {
                        "field": "mel_thick_mm",
                        "ranges": [
                            {"from": 0.0, "to": 0.5},
                            {"from": 0.5, "to": 1.0},
                            {"from": 1.0, "to": 1.5},
                            {"from": 1.5, "to": 2.0},
                            {"from": 2.0, "to": 2.5},
                            {"from": 2.5, "to": 3.0},
                            {"from": 3.0, "to": 3.5},
                            {"from": 3.5, "to": 4.0},
                            {"from": 4.0, "to": 4.5},
                            {"from": 4.5, "to": 5.0},
                            {"from": 5.0},
                        ],
                    }
                },
            )
        ),
    }
)

for field in FIELD_REGISTRY.keys():
    if field in [
        "blurry",
        "color_tint",
        "dermoscopic_type",
        "hairy",
        "image_type",
        "marker_pen",
    ]:
        FIELD_REGISTRY[field].type = "acquisition"
    else:
        FIELD_REGISTRY[field].type = "clinical"

for field, label in [
    ("anatom_site_general", "Anatomic Site"),
]:
    FIELD_REGISTRY[field].label = label
