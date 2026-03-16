from unittest.mock import Mock, patch

# # remove after checks
# def test_get_route_distance():
#     """
#     test_get_route_distance function.

#     Args:
#         None

#     Returns:
#         Any: Function result.
#     """
#     from functions.map.get_route_distance import get_route_distance

#     mock_response = Mock()
#     mock_response.raise_for_status.return_value = None
#     mock_response.json.return_value = {
#         "routes": [{"distance": 4500.0}]
#     }

#     with patch("functions.map.get_route_distance.requests.get", return_value=mock_response):
#         result = get_route_distance(40.7128, -74.0060, 34.0522, -118.2437)

#     assert isinstance(result, dict)
#     assert isinstance(result["distance_km"], float)
#     assert result["distance_km"] == 4.5


# New tests for route_distance
from unittest.mock import Mock, patch
from functions.map.get_route_distance import get_route_distance

def test_get_route_distance_success():
    """Test successful distance calculation using location names."""
    
    # 1. Mock Geocoding Response (Open-Meteo)
    mock_geo_response = Mock()
    mock_geo_response.json.return_value = {
        "results": [{"latitude": 40.71, "longitude": -74.00}]
    }
    mock_geo_response.raise_for_status.return_value = None

    # 2. Mock OSRM Routing Response
    mock_osrm_response = Mock()
    mock_osrm_response.json.return_value = {
        "routes": [{"distance": 5000.0}] # 5km
    }
    mock_osrm_response.raise_for_status.return_value = None

    # We use side_effect to return different responses for the sequential calls
    with patch("requests.get") as mock_get:
        mock_get.side_effect = [mock_geo_response, mock_geo_response, mock_osrm_response]
        
        result = get_route_distance("New York", "Los Angeles")

    assert isinstance(result, dict)
    assert result["distance_km"] == 5.0
    assert result["start"]["name"] == "New York"
    assert "error" not in result

def test_get_route_distance_invalid_location():
    """Test error handling when a location is not found."""
    
    # Mock Geocoding returning no results
    mock_empty_geo = Mock()
    mock_empty_geo.json.return_value = {"results": None}
    mock_empty_geo.raise_for_status.return_value = None

    with patch("requests.get", return_value=mock_empty_geo):
        result = get_route_distance("FakeCity123", "London")

    assert "error" in result
    assert "Could not find coordinates" in result["error"]


def test_reverse_geocode():
    """
    test_reverse_geocode function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.map.reverse_geocode import reverse_geocode

    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "display_name": "New York, New York County, New York, United States",
        "address": {"city": "New York", "state": "New York"}
    }

    with patch("functions.map.reverse_geocode.requests.get", return_value=mock_response):
        result = reverse_geocode(40.7128, -74.0060)

    assert isinstance(result, dict)
    assert "address" in result
    assert isinstance(result["address"], str)
    assert "New York" in result["address"]