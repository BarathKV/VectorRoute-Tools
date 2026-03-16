import requests
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

def get_timezone_from_name(location_name: str):
    """Helper to fetch the IANA timezone for a location name."""
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": location_name, "count": 1, "language": "en", "format": "json"}
    
    response = requests.get(geo_url, params=params, timeout=10)
    response.raise_for_status()
    results = response.json().get("results")
    
    if not results or "timezone" not in results[0]:
        return None
    return results[0]["timezone"]

def convert_time_between_locations(time_str: str, from_location: str, to_location: str):
    """
    Convert time from one city/location to another.
    
    Args:
        time_str (str): "YYYY-MM-DD HH:MM"
        from_location (str): e.g., "Kolkata"
        to_location (str): e.g., "Dubai"
    """
    # 1. Resolve Locations to Timezones
    tz_from_name = get_timezone_from_name(from_location)
    tz_to_name = get_timezone_from_name(to_location)
    
    if not tz_from_name:
        return {"error": f"Could not find timezone for: {from_location}"}
    if not tz_to_name:
        return {"error": f"Could not find timezone for: {to_location}"}

    try:
        # 2. Localize and Convert
        dt_naive = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        dt_from = dt_naive.replace(tzinfo=ZoneInfo(tz_from_name))
        dt_to = dt_from.astimezone(ZoneInfo(tz_to_name))
        
        return {
            "original_time": time_str,
            "from": {"location": from_location, "timezone": tz_from_name},
            "to": {"location": to_location, "timezone": tz_to_name},
            "converted_time": dt_to.strftime("%Y-%m-%d %H:%M")
        }
    except Exception as e:
        return {"error": str(e)}