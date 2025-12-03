import pandas as pd
import pytest
from unittest.mock import patch
from logic.fetch_order_information import fetch_order_by_id, fetch_order_by_email
from langchain.tools import tool

# replace actual customer information with mock csv dataset
TEST_DF = pd.DataFrame([
    {"order_id": "123", "email": "test@example.com", "status": "shipped"},
    {"order_id": "456", "email": "other@example.com", "status": "delivered"}
])


# Look up the order by id, happy flow
def test_fetch_order_by_id_happy():
    #replace an actual order.csv file with a mock dataset using patch
    with patch("pandas.read_csv", return_value=TEST_DF):
        result = fetch_order_by_id("123")

    #verify that the information was sucesfully fetched
    assert result["order_id"][0] == "123"
    assert result["email"][0] == "test@example.com"
    assert result["status"][0] == "shipped"


#Look up the order by email, unhappy flow
def test_fetch_order_by_email_happy():
    #replace an actual order.csv file with a mock dataset using patch
    with patch("pandas.read_csv", return_value=TEST_DF):
        result = fetch_order_by_email("other@example.com")

    assert result["order_id"][1] == "456"
    assert result["status"][1] == "delivered"


# Unhappy flow - simulate an exception when reading a file, return an empty dict
def test_fetch_order_unhappy_file_error():
    with patch("pandas.read_csv", side_effect=Exception("file missing")):
        result = fetch_order_by_id("999999")

    assert result == {}