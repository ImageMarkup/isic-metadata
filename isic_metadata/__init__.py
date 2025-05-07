from __future__ import annotations

import contextlib
from dataclasses import dataclass
from importlib.metadata import PackageNotFoundError, version
from typing import Any, Literal

with contextlib.suppress(PackageNotFoundError):
    __version__ = version("isic-metadata")


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
    "anatom_site_special",
    "color_tint",
    "patient_id",
    "lesion_id",
    "rcm_case_id",
    "image_manipulation",
]:
    FIELD_REGISTRY[field] = Field(
        search=SearchConfig(
            key=field,
            es_property={"type": "keyword"},
            es_facet={"terms": {"field": field}},
        )
    )


FIELD_REGISTRY.update(
    {
        "fitzpatrick_skin_type": Field(
            search=SearchConfig(
                key="fitzpatrick_skin_type",
                es_property={"type": "keyword"},
                es_facet={
                    "terms": {
                        "field": "fitzpatrick_skin_type",
                        "order": {"_key": "asc"},
                    }
                },
            )
        ),
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
        "diagnosis_1": Field(
            search=SearchConfig(
                key="diagnosis_1",
                es_property={"type": "keyword"},
                es_facet={"terms": {"field": "diagnosis_1", "size": 100}},
            )
        ),
        "diagnosis_2": Field(
            search=SearchConfig(
                key="diagnosis_2",
                es_property={"type": "keyword"},
                es_facet={"terms": {"field": "diagnosis_2", "size": 100}},
            )
        ),
        "diagnosis_3": Field(
            search=SearchConfig(
                key="diagnosis_3",
                es_property={"type": "keyword"},
                es_facet={"terms": {"field": "diagnosis_3", "size": 100}},
            )
        ),
        "diagnosis_4": Field(
            search=SearchConfig(
                key="diagnosis_4",
                es_property={"type": "keyword"},
                es_facet={"terms": {"field": "diagnosis_4", "size": 100}},
            )
        ),
        "diagnosis_5": Field(
            search=SearchConfig(
                key="diagnosis_5",
                es_property={"type": "keyword"},
                es_facet={"terms": {"field": "diagnosis_5", "size": 100}},
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

for field in FIELD_REGISTRY:  # noqa: PLC0206
    if field in [
        "blurry",
        "color_tint",
        "dermoscopic_type",
        "hairy",
        "image_type",
        "marker_pen",
        "image_manipulation",
    ]:
        FIELD_REGISTRY[field].type = "acquisition"
    else:
        FIELD_REGISTRY[field].type = "clinical"

for field, label in [
    ("anatom_site_general", "Anatomic Site"),
]:
    FIELD_REGISTRY[field].label = label
