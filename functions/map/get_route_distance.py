import requests

def get_coordinates(location_name: str):
    """Helper to fetch lat/long for a given location name."""
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": location_name, "count": 1, "language": "en", "format": "json"}
    
    response = requests.get(geo_url, params=params, timeout=10)
    response.raise_for_status()
    results = response.json().get("results")
    
    if not results:
        return None
    return results[0]["latitude"], results[0]["longitude"]

def get_route_distance(start_location: str, end_location: str):
    """
    Calculate road route distance between two named locations.
    """
    # 1. Geocode Start Location
    start_coords = get_coordinates(start_location)
    if not start_coords:
        return {"error": f"Could not find coordinates for start location: {start_location}"}
    
    # 2. Geocode End Location
    end_coords = get_coordinates(end_location)
    if not end_coords:
        return {"error": f"Could not find coordinates for end location: {end_location}"}

    start_lat, start_lon = start_coords
    end_lat, end_lon = end_coords

    # 3. Calculate Route
    osrm_url = (
        f"https://router.project-osrm.org/route/v1/driving/"
        f"{start_lon},{start_lat};{end_lon},{end_lat}"
    )
    
    response = requests.get(osrm_url, params={"overview": "false"}, timeout=10)
    response.raise_for_status()
    data = response.json()

    routes = data.get("routes")
    if not routes:
        return {"error": "No road route found between these locations"}

    distance_km = routes[0]["distance"] / 1000

    return {
        "start": {"name": start_location, "lat": start_lat, "lon": start_lon},
        "end": {"name": end_location, "lat": end_lat, "lon": end_lon},
        "distance_km": round(distance_km, 2)
    }