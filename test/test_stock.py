import pytest
import sys
from pathlib import Path
from unittest.mock import Mock, patch

# Add parent directory to path so we can import functions
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_get_crypto_price():
    from functions.stock.get_crypto_price import get_crypto_price

    # Test case 1: Expected output check
    coin_id = "bitcoin"
    vs_currency = "usd"

    api_response = Mock()
    api_response.raise_for_status.return_value = None
    api_response.json.return_value = {
        "bitcoin": {
            "usd": 64250.55,
            "usd_market_cap": 1260000000000,
            "usd_24h_vol": 27500000000,
            "usd_24h_change": 1.84,
        }
    }

    with patch("requests.get", return_value=api_response):
        result = get_crypto_price(coin_id, vs_currency)

    expected_result = {
        "coin_id": "bitcoin",
        "vs_currency": "usd",
        "price": 64250.55,
        "market_cap": 1260000000000,
        "volume_24h": 27500000000,
        "change_24h_percent": 1.84,
    }
    assert result == expected_result

    # Test case 2: Invalid coin should raise ValueError
    invalid_response = Mock()
    invalid_response.raise_for_status.return_value = None
    invalid_response.json.return_value = {}

    with patch("requests.get", return_value=invalid_response):
        with pytest.raises(ValueError):
            get_crypto_price("invalidcoin")


def test_get_market_movers():
    from functions.stock.get_market_movers import get_market_movers

    # Test case 1: Expected output check
    api_response = Mock()
    api_response.raise_for_status.return_value = None
    api_response.json.return_value = {
        "quoteResponse": {
            "result": [
                {
                    "symbol": "AAA",
                    "shortName": "AAA Corp",
                    "regularMarketPrice": 100.0,
                    "regularMarketChange": 5.0,
                    "regularMarketChangePercent": 5.0,
                },
                {
                    "symbol": "BBB",
                    "shortName": "BBB Inc",
                    "regularMarketPrice": 50.0,
                    "regularMarketChange": -3.0,
                    "regularMarketChangePercent": -6.0,
                },
                {
                    "symbol": "CCC",
                    "shortName": "CCC Ltd",
                    "regularMarketPrice": 80.0,
                    "regularMarketChange": 1.0,
                    "regularMarketChangePercent": 1.2,
                },
            ]
        }
    }

    with patch("requests.get", return_value=api_response):
        result = get_market_movers(limit=2)

    assert result["watchlist_count"] == 3
    assert result["top_gainers"][0]["symbol"] == "AAA"
    assert result["top_gainers"][1]["symbol"] == "CCC"
    assert result["top_losers"][0]["symbol"] == "BBB"


def test_compare_stocks():
    from functions.stock.compare_stocks import compare_stocks

    # Test case 1: Expected output check
    symbols = ["AAPL", "MSFT", "GOOGL"]

    api_response = Mock()
    api_response.raise_for_status.return_value = None
    api_response.json.return_value = {
        "quoteResponse": {
            "result": [
                {
                    "symbol": "AAPL",
                    "regularMarketPrice": 210.0,
                    "regularMarketChange": 1.5,
                    "regularMarketChangePercent": 0.72,
                    "currency": "USD",
                },
                {
                    "symbol": "MSFT",
                    "regularMarketPrice": 415.0,
                    "regularMarketChange": 4.8,
                    "regularMarketChangePercent": 1.17,
                    "currency": "USD",
                },
                {
                    "symbol": "GOOGL",
                    "regularMarketPrice": 175.0,
                    "regularMarketChange": -2.1,
                    "regularMarketChangePercent": -1.18,
                    "currency": "USD",
                },
            ]
        }
    }

    with patch("requests.get", return_value=api_response):
        result = compare_stocks(symbols)

    assert result["requested_symbols"] == ["AAPL", "MSFT", "GOOGL"]
    assert len(result["results"]) == 3
    assert result["best_performer"]["symbol"] == "MSFT"
    assert result["worst_performer"]["symbol"] == "GOOGL"

    # Test case 2: Empty symbols should raise ValueError
    with pytest.raises(ValueError):
        compare_stocks([])


def test_get_dividend_info():
    from functions.stock.get_dividend_info import get_dividend_info

    # Test case 1: Expected output check
    api_response = Mock()
    api_response.raise_for_status.return_value = None
    api_response.json.return_value = {
        "quoteResponse": {
            "result": [
                {
                    "symbol": "AAPL",
                    "regularMarketPrice": 210.0,
                    "currency": "USD",
                    "trailingAnnualDividendRate": 0.96,
                    "trailingAnnualDividendYield": 0.0046,
                    "exDividendDate": 1735603200,
                }
            ]
        }
    }

    with patch("requests.get", return_value=api_response):
        result = get_dividend_info("aapl")

    expected_result = {
        "symbol": "AAPL",
        "price": 210.0,
        "currency": "USD",
        "dividend_rate": 0.96,
        "dividend_yield": 0.0046,
        "ex_dividend_date": 1735603200,
    }
    assert result == expected_result

    # Test case 2: Invalid symbol should raise ValueError
    invalid_response = Mock()
    invalid_response.raise_for_status.return_value = None
    invalid_response.json.return_value = {"quoteResponse": {"result": []}}

    with patch("requests.get", return_value=invalid_response):
        with pytest.raises(ValueError):
            get_dividend_info("INVALID")


if __name__ == "__main__":
    test_get_crypto_price()
    test_get_market_movers()
    test_compare_stocks()
    test_get_dividend_info()
