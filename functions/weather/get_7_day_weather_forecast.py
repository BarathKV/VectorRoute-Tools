import requests

def get_7_day_weather_forecast(city: str):
    """
    Get a 7-day weather forecast for a given city using wttr.in (no API key required).
    
    Args:
        city (str): Name of the city to get the weather forecast for
        
    Returns:
        dict: Dictionary containing city name and 7-day forecast with temperature ranges,
              weather conditions, and sun hours for each day
    """
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    weather = data["weather"]
    
    forecast = []
    for day in weather:
        daily_forecast = {
            "date": day["date"],
            "max_temp_c": day["maxtempC"],
            "min_temp_c": day["mintempC"],
            "avg_temp_c": day["avgtempC"],
            "weather_description": day["hourly"][0]["weatherDesc"][0]["value"],
            "humidity": day["hourly"][0]["humidity"],
            "sun_hours": day["sunHour"],
            "uv_index": day["uvIndex"],
            "wind_kph": day["hourly"][0]["windspeedKmph"]
        }
        forecast.append(daily_forecast)
    
    return {
        "city": city,
        "forecast": forecast,
        "days_count": len(forecast)
    }
