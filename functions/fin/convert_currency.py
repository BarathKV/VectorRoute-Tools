import requests

def convert_currency(from_currency: str, to_currency: str, amount: float):
    """
    Convert an amount from one currency to another using Frankfurter API (free, no key required).
    
    Args:
        from_currency: Source currency code (e.g., 'USD')
        to_currency: Target currency code (e.g., 'EUR')
        amount: Amount to convert
    
    Returns:
        Dictionary with conversion details
    """
    url = f"https://api.frankfurter.dev/v1/latest"
    params = {
        "base": from_currency.upper(),
        "symbols": to_currency.upper(),
        "amount": amount
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Check if the API returned a successful response
        if "rates" not in data:
            raise ValueError(f"API Error: Unable to fetch exchange rate")
        
        converted_amount = data["rates"][to_currency.upper()] * amount
        rate = data["rates"][to_currency.upper()]
        
        return {
            "from": from_currency.upper(),
            "to": to_currency.upper(),
            "amount": amount,
            "converted_amount": round(converted_amount, 2),
            "rate": round(rate, 4)
        }
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch exchange rate: {str(e)}")


