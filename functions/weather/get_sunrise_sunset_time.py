import requests


def get_sunrise_sunset_time(city: str):
    """
    Get sunrise and sunset timing for a given city using Open-Meteo APIs (no API key required).

    Args:
        city (str): Name of the city to get sunrise and sunset time for

    Returns:
        dict: Dictionary containing city name, forecast date, sunrise and sunset timing details
    """
    geocode_url = "https://geocoding-api.open-meteo.com/v1/search"
    geocode_response = requests.get(
        geocode_url,
        params={"name": city, "count": 1, "language": "en", "format": "json"},
        timeout=10,
    )
    geocode_response.raise_for_status()

    geocode_data = geocode_response.json()
    results = geocode_data.get("results")
    if not results:
        raise ValueError(f"City not found: {city}")

    location = results[0]
    latitude = location["latitude"]
    longitude = location["longitude"]
    resolved_city = location["name"]

    forecast_url = "https://api.open-meteo.com/v1/forecast"
    forecast_response = requests.get(
        forecast_url,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "daily": "sunrise,sunset",
            "timezone": "auto",
        },
        timeout=10,
    )
    forecast_response.raise_for_status()

    data = forecast_response.json()
    daily = data["daily"]

    return {
        "city": resolved_city,
        "date": daily["time"][0],
        "sunrise": daily["sunrise"][0],
        "sunset": daily["sunset"][0],
    }
