import requests


def get_uv_index(city: str):
    """
    Get UV index details for a given city using Open-Meteo APIs (no API key required).

    Args:
        city (str): Name of the city to get UV index for

    Returns:
        dict: Dictionary containing city name and current/daily UV index details
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
            "current": "uv_index",
            "daily": "uv_index_max,uv_index_clear_sky_max",
            "timezone": "auto",
        },
        timeout=10,
    )
    forecast_response.raise_for_status()

    data = forecast_response.json()
    current = data["current"]
    daily = data["daily"]

    return {
        "city": resolved_city,
        "date": daily["time"][0],
        "current_uv_index": current.get("uv_index"),
        "max_uv_index": daily["uv_index_max"][0],
        "clear_sky_max_uv_index": daily["uv_index_clear_sky_max"][0],
    }
