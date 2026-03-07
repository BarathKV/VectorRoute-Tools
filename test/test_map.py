from unittest.mock import Mock, patch


def test_get_route_distance():
    from functions.map.get_route_distance import get_route_distance

    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "routes": [{"distance": 4500.0}]
    }

    with patch("functions.map.get_route_distance.requests.get", return_value=mock_response):
        result = get_route_distance(40.7128, -74.0060, 34.0522, -118.2437)

    assert isinstance(result, dict)
    assert isinstance(result["distance_km"], float)
    assert result["distance_km"] == 4.5


def test_reverse_geocode():
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