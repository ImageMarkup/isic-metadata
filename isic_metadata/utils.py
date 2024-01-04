from typing import Sequence

from isic_metadata.metadata import MetadataRow


def get_unstructured_columns(column_names: Sequence[str]) -> list[str]:
    reserved_columns = set(["filename", "isic_id"])
    return sorted(list(set(column_names) - set(MetadataRow.model_fields.keys()) - reserved_columns))
