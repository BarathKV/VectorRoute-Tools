import requests


def get_market_movers(limit: int = 5):
    """
    Get market movers from a predefined watchlist using Yahoo Finance quote endpoint (no API key required).

    Args:
        limit (int): Number of top gainers and losers to return

    Returns:
        dict: Dictionary containing top gainers and top losers with symbol and price-change details
    """
    symbols = [
        "AAPL",
        "MSFT",
        "GOOGL",
        "AMZN",
        "META",
        "TSLA",
        "NVDA",
        "NFLX",
        "AMD",
        "INTC",
        "JPM",
        "V",
        "WMT",
        "DIS",
        "BA",
    ]

    url = "https://query1.finance.yahoo.com/v7/finance/quote"
    response = requests.get(url, params={"symbols": ",".join(symbols)}, timeout=10)
    response.raise_for_status()

    data = response.json()
    quotes = data.get("quoteResponse", {}).get("result", [])

    formatted = []
    for quote in quotes:
        change_percent = quote.get("regularMarketChangePercent")
        if change_percent is None:
            continue

        formatted.append(
            {
                "symbol": quote.get("symbol"),
                "name": quote.get("shortName"),
                "price": quote.get("regularMarketPrice"),
                "change": quote.get("regularMarketChange"),
                "change_percent": change_percent,
            }
        )

    formatted.sort(key=lambda item: item["change_percent"], reverse=True)
    top_gainers = formatted[:limit]
    top_losers = list(reversed(formatted[-limit:]))

    return {
        "watchlist_count": len(formatted),
        "top_gainers": top_gainers,
        "top_losers": top_losers,
    }
