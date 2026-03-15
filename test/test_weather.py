import pytest
import sys
from pathlib import Path
from unittest.mock import Mock, patch

# Add parent directory to path so we can import functions
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_get_historical_weather():
    """
    test_get_historical_weather function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.weather.get_historical_weather import get_historical_weather

    # Test case 1: Expected output check
    city = "London"
    date = "2025-01-10"

    geocode_response = Mock()
    geocode_response.raise_for_status.return_value = None
    geocode_response.json.return_value = {
        "results": [{"name": "London", "latitude": 51.5074, "longitude": -0.1278}]
    }

    archive_response = Mock()
    archive_response.raise_for_status.return_value = None
    archive_response.json.return_value = {
        "daily": {
            "time": ["2025-01-10"],
            "temperature_2m_max": [11.2],
            "temperature_2m_min": [3.1],
            "temperature_2m_mean": [7.0],
            "precipitation_sum": [2.4],
            "weathercode": [61],
        }
    }

    with patch("requests.get", side_effect=[geocode_response, archive_response]):
        result = get_historical_weather(city, date)

    expected_result = {
        "city": "London",
        "date": "2025-01-10",
        "max_temp_c": 11.2,
        "min_temp_c": 3.1,
        "avg_temp_c": 7.0,
        "precipitation_mm": 2.4,
        "weather_code": 61,
    }
    assert result == expected_result

    # Test case 2: Invalid city should raise ValueError
    empty_geocode_response = Mock()
    empty_geocode_response.raise_for_status.return_value = None
    empty_geocode_response.json.return_value = {"results": []}

    with patch("requests.get", return_value=empty_geocode_response):
        with pytest.raises(ValueError):
            get_historical_weather("InvalidCityNameShouldNotExist123", date)


def test_get_uv_index():
    """
    test_get_uv_index function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.weather.get_uv_index import get_uv_index

    # Test case 1: Expected output check
    city = "New York"
    geocode_response = Mock()
    geocode_response.raise_for_status.return_value = None
    geocode_response.json.return_value = {
        "results": [{"name": "New York", "latitude": 40.7128, "longitude": -74.0060}]
    }

    forecast_response = Mock()
    forecast_response.raise_for_status.return_value = None
    forecast_response.json.return_value = {
        "current": {"uv_index": 2.7},
        "daily": {
            "time": ["2025-01-10"],
            "uv_index_max": [4.8],
            "uv_index_clear_sky_max": [5.4],
        },
    }

    with patch("requests.get", side_effect=[geocode_response, forecast_response]):
        result = get_uv_index(city)

    expected_result = {
        "city": "New York",
        "date": "2025-01-10",
        "current_uv_index": 2.7,
        "max_uv_index": 4.8,
        "clear_sky_max_uv_index": 5.4,
    }
    assert result == expected_result

    # Test case 2: Invalid city should raise ValueError
    empty_geocode_response = Mock()
    empty_geocode_response.raise_for_status.return_value = None
    empty_geocode_response.json.return_value = {"results": []}

    with patch("requests.get", return_value=empty_geocode_response):
        with pytest.raises(ValueError):
            get_uv_index("InvalidCityNameShouldNotExist123")


def test_get_sunrise_sunset_time():
    """
    test_get_sunrise_sunset_time function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.weather.get_sunrise_sunset_time import get_sunrise_sunset_time

    # Test case 1: Expected output check
    city = "Tokyo"
    geocode_response = Mock()
    geocode_response.raise_for_status.return_value = None
    geocode_response.json.return_value = {
        "results": [{"name": "Tokyo", "latitude": 35.6762, "longitude": 139.6503}]
    }

    forecast_response = Mock()
    forecast_response.raise_for_status.return_value = None
    forecast_response.json.return_value = {
        "daily": {
            "time": ["2025-01-10"],
            "sunrise": ["2025-01-10T06:50"],
            "sunset": ["2025-01-10T16:45"],
        }
    }

    with patch("requests.get", side_effect=[geocode_response, forecast_response]):
        result = get_sunrise_sunset_time(city)

    expected_result = {
        "city": "Tokyo",
        "date": "2025-01-10",
        "sunrise": "2025-01-10T06:50",
        "sunset": "2025-01-10T16:45",
    }
    assert result == expected_result

    # Test case 2: Invalid city should raise ValueError
    empty_geocode_response = Mock()
    empty_geocode_response.raise_for_status.return_value = None
    empty_geocode_response.json.return_value = {"results": []}

    with patch("requests.get", return_value=empty_geocode_response):
        with pytest.raises(ValueError):
            get_sunrise_sunset_time("InvalidCityNameShouldNotExist123")


if __name__ == "__main__":
    test_get_historical_weather()
    test_get_uv_index()
    test_get_sunrise_sunset_time()
