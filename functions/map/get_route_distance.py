import requests
from geopy.geocoders import Nominatim

def get_route_distance(start_place: str, end_place: str):
    """
    Calculate road route distance between two places (as strings) using geocoding and OSRM.
    """
    try:
        # Geocode the place names to coordinates
        geolocator = Nominatim(user_agent="routetools_demo")
        start_loc = geolocator.geocode(start_place, timeout=10)
        end_loc = geolocator.geocode(end_place, timeout=10)
        
        if not start_loc or not end_loc:
            raise ValueError("Could not geocode one or both locations")
        
        start_lat, start_lon = start_loc.latitude, start_loc.longitude
        end_lat, end_lon = end_loc.latitude, end_loc.longitude
        
        # Get route distance using OSRM
        url = (
            "https://router.project-osrm.org/route/v1/driving/"
            f"{start_lon},{start_lat};{end_lon},{end_lat}"
        )
        
        params = {"overview": "false"}
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        routes = data.get("routes")
        if not routes:
            raise ValueError("No route found")
        
        distance_meters = routes[0]["distance"]
        distance_km = distance_meters / 1000
        
        return round(distance_km, 2)
    except Exception as e:
        raise Exception(f"Failed to calculate route distance: {str(e)}")
