import pandas as pd
def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validate the DataFrame by checking missing values
    and duplicate rows.

    Args:
        df: Input Pandas DataFrame.

    Returns:
        Original DataFrame after displaying validation results.
    """
    print("Missing values:")
    print(df.isnull().sum())

    print("Duplicate rows:", df.duplicated().sum())

    return df

# Task 4: Convert column names to snake_case

def to_snake_case(column_name):
    column_name = column_name.strip().lower()
    column_name = column_name.replace(" ", "_")
    column_name = column_name.replace("-", "_")
    return column_name


# Task 5: Map columns to standard schema

def map_columns(
    data: list[dict],
    mapping: dict[str, str]
) -> list[dict]:
    """
    Map source column names to standard column names.

    Args:
        data: List of dictionaries containing source records.
        mapping: Dictionary containing old and new column names.

    Returns:
        List of dictionaries with mapped column names.
    """
    new_data = []

    for row in data:
        new_row = {}

        for old_name, new_name in mapping.items():
            if old_name in row:
                new_row[new_name] = row[old_name]

        new_data.append(new_row)

    return new_data

