import pytest
import sys
from pathlib import Path
from unittest.mock import Mock, patch
from datetime import datetime

# Add parent directory to path so we can import functions
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_get_current_time():
    from functions.time_operations.get_current_time import get_current_time

    # Test case 1: Verify structure and time validity
    mock_time = datetime(2025, 2, 28, 14, 30, 45, 123456).time()
    
    with patch("functions.time_operations.get_current_time.datetime") as mock_datetime:
        mock_datetime.now.return_value.time.return_value = mock_time
        result = get_current_time()

    assert result["hour"] == 14
    assert result["minute"] == 30
    assert result["second"] == 45
    assert result["microsecond"] == 123456


def test_convert_time_format():
    from functions.time_operations.convert_time_format import convert_time_format

    # Test case 1: 24-hour to 12-hour format
    result = convert_time_format("14:30:00", "%H:%M:%S", "%I:%M:%S %p")
    
    expected = {
        "original_time": "14:30:00",
        "input_format": "%H:%M:%S",
        "converted_time": "02:30:00 PM",
        "output_format": "%I:%M:%S %p",
    }
    assert result == expected

    # Test case 2: Another format
    result = convert_time_format("09:15:30", "%H:%M:%S", "%I:%M:%S %p")
    assert result["converted_time"] == "09:15:30 AM"


def test_add_hours():
    from functions.time_operations.add_hours import add_hours

    # Test case 1: Add positive hours
    result = add_hours("14:30:00", 3)
    
    expected = {
        "original_time": "14:30:00",
        "hours_added": 3,
        "result_time": "17:30:00",
        "result_datetime": "1900-01-01T17:30:00",
    }
    assert result == expected

    # Test case 2: Add hours crossing midnight
    result = add_hours("22:30:00", 5)
    assert result["result_time"] == "03:30:00"


def test_subtract_hours():
    from functions.time_operations.subtract_hours import subtract_hours

    # Test case 1: Subtract positive hours
    result = subtract_hours("14:30:00", 3)
    
    expected = {
        "original_time": "14:30:00",
        "hours_subtracted": 3,
        "result_time": "11:30:00",
        "result_datetime": "1900-01-01T11:30:00",
    }
    assert result == expected

    # Test case 2: Subtract hours crossing before midnight
    result = subtract_hours("02:30:00", 5)
    assert result["result_time"] == "21:30:00"


def test_calculate_time_difference():
    from functions.time_operations.calculate_time_difference import calculate_time_difference

    # Test case 1: Positive difference
    result = calculate_time_difference("10:30:00", "14:30:00")
    
    expected = {
        "time1": "10:30:00",
        "time2": "14:30:00",
        "hours_difference": 4,
        "minutes_difference": 0,
        "seconds_difference": 0,
        "total_seconds": 14400,
    }
    assert result == expected

    # Test case 2: Difference with minutes and seconds
    result = calculate_time_difference("10:30:15", "14:45:45")
    assert result["hours_difference"] == 4
    assert result["minutes_difference"] == 15
    assert result["seconds_difference"] == 30


def test_is_valid_time():
    from functions.time_operations.is_valid_time import is_valid_time

    # Test case 1: Valid time
    result = is_valid_time("14:30:00")
    
    expected = {
        "time_string": "14:30:00",
        "format": "%H:%M:%S",
        "is_valid": True,
        "hour": 14,
        "minute": 30,
        "second": 0,
    }
    assert result == expected

    # Test case 2: Invalid time
    result = is_valid_time("25:30:00")
    assert result["is_valid"] is False
    assert "error" in result


def test_convert_to_24_hour():
    from functions.time_operations.convert_to_24_hour import convert_to_24_hour

    # Test case 1: PM time conversion
    result = convert_to_24_hour("02:30:00 PM")
    
    expected = {
        "original_time": "02:30:00 PM",
        "original_format": "12-hour",
        "converted_time": "14:30:00",
        "converted_format": "24-hour",
    }
    assert result == expected

    # Test case 2: AM time conversion
    result = convert_to_24_hour("09:15:00 AM")
    assert result["converted_time"] == "09:15:00"

    # Test case 3: Invalid format
    with pytest.raises(ValueError):
        convert_to_24_hour("25:30:00")


def test_convert_to_12_hour():
    from functions.time_operations.convert_to_12_hour import convert_to_12_hour

    # Test case 1: Afternoon time
    result = convert_to_12_hour("14:30:00")
    
    expected = {
        "original_time": "14:30:00",
        "original_format": "24-hour",
        "converted_time": "02:30:00 PM",
        "converted_format": "12-hour",
    }
    assert result == expected

    # Test case 2: Morning time
    result = convert_to_12_hour("09:15:00")
    assert result["converted_time"] == "09:15:00 AM"

    # Test case 3: Invalid format
    with pytest.raises(ValueError):
        convert_to_12_hour("25:30:00")


def test_get_timestamp():
    from functions.time_operations.get_timestamp import get_timestamp

    # Test case 1: Verify timestamp structure
    with patch("functions.time_operations.get_timestamp.time") as mock_time:
        mock_time.time.return_value = 1740696645.5

        result = get_timestamp()

    expected = {
        "timestamp": 1740696645.5,
        "timestamp_int": 1740696645,
        "milliseconds": 1740696645500,
    }
    assert result == expected


def test_timestamp_to_time():
    from functions.time_operations.timestamp_to_time import timestamp_to_time

    # Test case 1: Convert timestamp to time (check structure and keys)
    result = timestamp_to_time(1740696645.0)
    
    assert result["timestamp"] == 1740696645.0
    # Hour depends on system timezone, just verify it's a valid hour (0-23)
    assert 0 <= result["hour"] <= 23
    assert 0 <= result["minute"] <= 59
    assert 0 <= result["second"] <= 59
    assert "full_datetime" in result
    assert "formatted_time" in result
    assert "time" in result

    # Test case 2: Custom format
    result = timestamp_to_time(1740696645.0, "%I:%M:%S %p")
    assert "formatted_time" in result
    assert ":" in result["formatted_time"]


if __name__ == "__main__":
    test_get_current_time()
    test_convert_time_format()
    test_add_hours()
    test_subtract_hours()
    test_calculate_time_difference()
    test_is_valid_time()
    test_convert_to_24_hour()
    test_convert_to_12_hour()
    test_get_timestamp()
    test_timestamp_to_time()
