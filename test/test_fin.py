import pytest


def test_calculate_loan_emi():
    from functions.fin.calculate_loan_emi import calculate_loan_emi
    # Test case 1: Basic test case
    principal = 100000
    annual_rate = 10
    tenure_years = 15
    expected_emi = 193428.92  # Calculated using the formula
    emi = calculate_loan_emi(principal, annual_rate, tenure_years)
    print(emi)
    assert round(emi["total_payment"], 2) == expected_emi, f"Expected {expected_emi}, got {emi}"

    # Test case 2: Zero interest rate
    principal = 50000
    annual_rate = 5
    tenure_years = 10
    expected_emi = 63639.31  # Principal divided by number of months
    emi = calculate_loan_emi(principal, annual_rate, tenure_years)
    print(emi)
    assert round(emi["total_payment"], 2) == expected_emi, f"Expected {expected_emi}, got {emi}"

def test_convert_currency():
    from functions.fin.convert_currency import convert_currency
    # Test case 1: Basic test case
    amount = 100
    from_currency = "USD"
    to_currency = "EUR"
    converted_amount = convert_currency(from_currency, to_currency,amount)
    print(converted_amount)
    assert isinstance(converted_amount["converted_amount"], float), "Converted amount should be a float"

    # Test case 2: Invalid currency code
    with pytest.raises(Exception):
        convert_currency(from_currency, "INVALID", amount)



def test_get_stock_price():
    from functions.fin.get_stock_price import get_stock_price
    # Test case 1: Basic test case
    stock_symbol = "AAPL"
    price = get_stock_price(stock_symbol)
    print(price)
    assert isinstance(price, float), "Stock price should be a float"

    # # Test case 2: Invalid stock symbol
    # try:
    #     get_stock_price("INVALID")
    #     assert False, "Expected an exception for invalid stock symbol"
    # except ValueError:
    #     pass  # Expected exception