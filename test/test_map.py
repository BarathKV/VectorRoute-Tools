def test_get_route_distance():
    from functions.map import get_route_distance
    distance = get_route_distance("New York, NY", "Los Angeles, CA")
    assert distance > 0, "Distance should be greater than 0"


def test_reverse_geocode():
    from functions.map import reverse_geocode
    location = reverse_geocode(40.7128, -74.0060)  # Coordinates for New York City
    assert "New York" in location, "Location should contain 'New York'"