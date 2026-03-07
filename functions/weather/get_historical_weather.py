import requests


def get_historical_weather(city: str, date: str):
    """
    Get historical weather for a given city and date using Open-Meteo APIs (no API key required).

    Args:
        city (str): Name of the city to get historical weather for
        date (str): Date in YYYY-MM-DD format

    Returns:
        dict: Dictionary containing city name, date, and historical weather summary
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

    archive_url = "https://archive-api.open-meteo.com/v1/archive"
    archive_response = requests.get(
        archive_url,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "start_date": date,
            "end_date": date,
            "daily": "temperature_2m_max,temperature_2m_min,temperature_2m_mean,precipitation_sum,weathercode",
            "timezone": "auto",
        },
        timeout=10,
    )
    archive_response.raise_for_status()

    data = archive_response.json()
    daily = data["daily"]

    return {
        "city": resolved_city,
        "date": daily["time"][0],
        "max_temp_c": daily["temperature_2m_max"][0],
        "min_temp_c": daily["temperature_2m_min"][0],
        "avg_temp_c": daily["temperature_2m_mean"][0],
        "precipitation_mm": daily["precipitation_sum"][0],
        "weather_code": daily["weathercode"][0],
    }
