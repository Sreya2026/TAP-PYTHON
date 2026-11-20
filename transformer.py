import pandas as pd
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows and replace missing values with zero.

    Args:
        df: Input DataFrame.

    Returns:
        Transformed DataFrame.
    """
    df = df.drop_duplicates()
    df = df.fillna(0)

    return df

def to_snake_case(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert DataFrame column names into snake_case.

    Args:
        df: Input DataFrame.

    Returns:
        DataFrame with standardized column names.
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    return df

def convert_data(data: list[dict]) -> list[dict]:
    """
    Convert data types for specific columns.

    Args:
        data: List of dictionaries containing order records.

    Returns:
        List of dictionaries with converted data types.
    """
    for row in data:
        row['price'] = float(row['price'])
        row['freight_value'] = float(row['freight_value'])
        row['order_purchase_timestamp'] = datetime.strptime(
            row['order_purchase_timestamp'], '%Y-%m-%d %H:%M:%S'
        )

    return data

from datetime import datetime

from datetime import datetime

def convert_data(data):
    for row in data:
        row['price'] = float(row['price'])
        row['freight_value'] = float(row['freight_value'])
        row['order_purchase_timestamp'] = datetime.strptime(
            row['order_purchase_timestamp'], '%Y-%m-%d %H:%M:%S'
        )
    return data


def calculate_order_total(data: list[dict]) -> dict:
    """
    Calculate the total amount for each order.

    Args:
        data: List of order records containing order_id,
              price and freight_value.

    Returns:
        Dictionary containing order IDs and their total amounts.
    """
    totals = {}

    for row in data:
        order_id = row['order_id']
        total = float(row['price']) + float(row['freight_value'])

        if order_id in totals:
            totals[order_id] += total
        else:
            totals[order_id] = total

    return totals

