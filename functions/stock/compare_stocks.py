import requests


def compare_stocks(symbols: list[str]):
    """
    Compare stock performance for multiple symbols using Yahoo Finance quote endpoint (no API key required).

    Args:
        symbols (list[str]): List of stock ticker symbols to compare

    Returns:
        dict: Dictionary containing per-symbol summary and best/worst performer by daily change percent
    """
    if not symbols:
        raise ValueError("At least one symbol is required")

    normalized_symbols = [symbol.strip().upper() for symbol in symbols if symbol and symbol.strip()]
    if not normalized_symbols:
        raise ValueError("At least one valid symbol is required")

    url = "https://query1.finance.yahoo.com/v7/finance/quote"
    response = requests.get(url, params={"symbols": ",".join(normalized_symbols)}, timeout=10)
    response.raise_for_status()

    data = response.json()
    quotes = data.get("quoteResponse", {}).get("result", [])

    comparison = []
    for quote in quotes:
        comparison.append(
            {
                "symbol": quote.get("symbol"),
                "price": quote.get("regularMarketPrice"),
                "change": quote.get("regularMarketChange"),
                "change_percent": quote.get("regularMarketChangePercent"),
                "currency": quote.get("currency"),
            }
        )

    if not comparison:
        raise ValueError("No valid stock data found for provided symbols")

    sortable = [item for item in comparison if item.get("change_percent") is not None]
    best_performer = max(sortable, key=lambda item: item["change_percent"]) if sortable else None
    worst_performer = min(sortable, key=lambda item: item["change_percent"]) if sortable else None

    return {
        "requested_symbols": normalized_symbols,
        "results": comparison,
        "best_performer": best_performer,
        "worst_performer": worst_performer,
    }
