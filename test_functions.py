import pandas as pd

from validator import validate_data, map_columns

from transformer import (
    transform_data,
    to_snake_case,
    convert_data,
    calculate_order_total
)


# Test 1: Validate data
def test_validate_data():

    df = pd.DataFrame({
        "name": ["Sreya", "Anu", "Sreya"],
        "age": [23, None, 23]
    })

    result = validate_data(df)

    assert result.equals(df)


# Test 2: Transform data
def test_transform_data():

    df = pd.DataFrame({
        "name": ["Sreya", "Anu", "Sreya"],
        "age": [23, None, 23]
    })

    result = transform_data(df)

    assert result.duplicated().sum() == 0
    assert result.isnull().sum().sum() == 0


# Test 3: Convert column name to snake_case
def test_to_snake_case():

    df = pd.DataFrame({
        "Customer Name": ["Sreya"],
        "Order-Date": ["2026-11-20"]
    })

    result = to_snake_case(df)

    assert list(result.columns) == [
        "customer_name",
        "order_date"
    ]


# Test 4: Convert data types
def test_convert_data():

    data = [
        {
            "price": "100.50",
            "freight_value": "20.50",
            "order_purchase_timestamp": "2026-11-20 10:30:00"
        }
    ]

    result = convert_data(data)

    assert isinstance(result[0]["price"], float)
    assert isinstance(result[0]["freight_value"], float)
    assert result[0]["price"] == 100.50
    assert result[0]["freight_value"] == 20.50


# Test 5: Calculate order total
def test_calculate_order_total():

    data = [
        {"order_id": "O1", "price": "100", "freight_value": "20"},
        {"order_id": "O1", "price": "200", "freight_value": "30"},
        {"order_id": "O2", "price": "150", "freight_value": "10"}
    ]

    result = calculate_order_total(data)

    assert result["O1"] == 350
    assert result["O2"] == 160


# Test 6: Map columns
def test_map_columns():

    data = [
        {"cust_id": 1, "cust_name": "Sreya"},
        {"cust_id": 2, "cust_name": "Anu"}
    ]

    mapping = {
        "cust_id": "customer_id",
        "cust_name": "customer_name"
    }

    result = map_columns(data, mapping)

    assert result[0]["customer_id"] == 1
    assert result[0]["customer_name"] == "Sreya"
    assert "cust_id" not in result[0]

    