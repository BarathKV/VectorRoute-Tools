def test_calculate_loan_emi():
    from functions.fin.calculate_loan_emi import calculate_loan_emi
    # Test case 1: Basic test case
    principal = 100000
    annual_rate = 10
    tenure_years = 15
    expected_emi = 1073.64  # Calculated using the formula
    emi = calculate_loan_emi(principal, annual_rate, tenure_years)
    assert round(emi, 2) == expected_emi, f"Expected {expected_emi}, got {emi}"

    # Test case 2: Zero interest rate
    principal = 50000
    annual_rate = 0
    tenure_years = 10
    expected_emi = 416.67  # Principal divided by number of months
    emi = calculate_loan_emi(principal, annual_rate, tenure_years)
    assert round(emi, 2) == expected_emi, f"Expected {expected_emi}, got {emi}"


def test_convert_currency():
    from functions.fin.convert_currency import convert_currency
    # Test case 1: Basic test case
    amount = 100
    from_currency = "USD"
    to_currency = "EUR"
    converted_amount = convert_currency(amount, from_currency, to_currency)
    assert isinstance(converted_amount, float), "Converted amount should be a float"

    # Test case 2: Invalid currency code
    try:
        convert_currency(amount, "INVALID", to_currency)
        assert False, "Expected an exception for invalid currency code"
    except ValueError:
        pass  # Expected exception



def test_get_stock_price():
    from functions.fin.get_stock_price import get_stock_price
    # Test case 1: Basic test case
    stock_symbol = "AAPL"
    price = get_stock_price(stock_symbol)
    assert isinstance(price, float), "Stock price should be a float"

    # Test case 2: Invalid stock symbol
    try:
        get_stock_price("INVALID")
        assert False, "Expected an exception for invalid stock symbol"
    except ValueError:
        pass  # Expected exception