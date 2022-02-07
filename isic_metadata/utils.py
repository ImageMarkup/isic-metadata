from isic_metadata.metadata import MetadataRow


def get_unstructured_columns(df):
    unstructured_columns = set()
    structured_columns = set(MetadataRow.__fields__.keys()) - {'unstructured'}

    for _, (_, row) in enumerate(df.iterrows(), start=2):
        unstructured_columns |= set(row.keys()) - structured_columns

    # unstructured columns are any columns that aren't part of the core
    # columns (filename, isic_id) and aren't defined in MetadataRow
    unstructured_columns -= {'filename', 'isic_id'}

    return sorted(list(unstructured_columns))
