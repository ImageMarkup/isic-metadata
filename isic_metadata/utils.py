from __future__ import annotations

from typing import TYPE_CHECKING

from isic_metadata.metadata import MetadataRow

if TYPE_CHECKING:
    from collections.abc import Sequence


def get_unstructured_columns(column_names: Sequence[str]) -> list[str]:
    reserved_columns = {"filename", "isic_id"}
    return sorted(set(column_names) - set(MetadataRow.model_fields.keys()) - reserved_columns)
