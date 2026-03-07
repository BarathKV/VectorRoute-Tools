import requests


def get_dividend_info(symbol: str):
    """
    Get dividend information for a stock symbol using Yahoo Finance quote endpoint (no API key required).

    Args:
        symbol (str): Stock ticker symbol (e.g., AAPL)

    Returns:
        dict: Dictionary containing dividend rate, dividend yield and ex-dividend date details
    """
    normalized_symbol = symbol.strip().upper()
    if not normalized_symbol:
        raise ValueError("Stock symbol is required")

    url = "https://query1.finance.yahoo.com/v7/finance/quote"
    response = requests.get(url, params={"symbols": normalized_symbol}, timeout=10)
    response.raise_for_status()

    data = response.json()
    quotes = data.get("quoteResponse", {}).get("result", [])
    if not quotes:
        raise ValueError(f"Stock symbol not found: {normalized_symbol}")

    quote = quotes[0]

    return {
        "symbol": quote.get("symbol"),
        "price": quote.get("regularMarketPrice"),
        "currency": quote.get("currency"),
        "dividend_rate": quote.get("trailingAnnualDividendRate"),
        "dividend_yield": quote.get("trailingAnnualDividendYield"),
        "ex_dividend_date": quote.get("exDividendDate"),
    }
