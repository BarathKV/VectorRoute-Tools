import requests


def get_crypto_price(coin_id: str, vs_currency: str = "usd"):
    """
    Get live crypto price details for a given coin from CoinGecko (no API key required).

    Args:
        coin_id (str): CoinGecko coin id (e.g., bitcoin, ethereum)
        vs_currency (str): Target fiat currency (e.g., usd, eur, inr)

    Returns:
        dict: Dictionary containing current price, 24h change and market cap details
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    response = requests.get(
        url,
        params={
            "ids": coin_id,
            "vs_currencies": vs_currency,
            "include_24hr_change": "true",
            "include_market_cap": "true",
            "include_24hr_vol": "true",
        },
        timeout=10,
    )
    response.raise_for_status()

    data = response.json()
    coin_data = data.get(coin_id)
    if not coin_data:
        raise ValueError(f"Coin not found: {coin_id}")

    return {
        "coin_id": coin_id,
        "vs_currency": vs_currency,
        "price": coin_data.get(vs_currency),
        "market_cap": coin_data.get(f"{vs_currency}_market_cap"),
        "volume_24h": coin_data.get(f"{vs_currency}_24h_vol"),
        "change_24h_percent": coin_data.get(f"{vs_currency}_24h_change"),
    }
