import requests

def get_stock_price(symbol: str):
    """
    Get the latest stock price for a symbol using Stooq API (free, no API key required).
    
    Args:
        symbol: Stock ticker symbol (e.g., 'AAPL', 'GOOGL')
    
    Returns:
        Dictionary with stock price details including OHLCV (Open, High, Low, Close, Volume)
        
    Raises:
        Exception: If API request fails or stock symbol not found
    """
    symbol = symbol.upper().strip()
    url = "https://stooq.com/q/l/"

    params = {
        "s": f"{symbol}.us",
        "f": "sd2t2ohlcv",
        "h": "",
        "e": "json"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "data" not in data or not data["data"]:
            raise ValueError(f"Stock symbol '{symbol}' not found or no data available")

        stock = data["data"][0]
        
        return {
            "symbol": stock.get("symbol"),
            "date": stock.get("date"),
            "time": stock.get("time"),
            "open": stock.get("open"),
            "high": stock.get("high"),
            "low": stock.get("low"),
            "close": stock.get("close"),
            "volume": stock.get("volume"),
            "change": round(stock.get("close", 0) - stock.get("open", 0), 2) if stock.get("close") and stock.get("open") else None,
            "change_percent": round(((stock.get("close", 0) - stock.get("open", 0)) / stock.get("open", 1) * 100), 2) if stock.get("close") and stock.get("open") else None
        }
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch stock price for {symbol}: {str(e)}")

