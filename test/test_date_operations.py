import pytest
import sys
from pathlib import Path
from unittest.mock import Mock, patch
from datetime import datetime, date

# Add parent directory to path so we can import functions
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_get_current_date():
    """
    test_get_current_date function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.date_operations.get_current_date import get_current_date

    # Test case 1: Verify structure and date validity
    mock_date = date(2025, 2, 28)
    
    with patch("functions.date_operations.get_current_date.datetime") as mock_datetime:
        mock_datetime.now.return_value.date.return_value = mock_date
        result = get_current_date()

    expected = {
        "date": "2025-02-28",
        "year": 2025,
        "month": 2,
        "day": 28,
    }
    assert result == expected


def test_get_current_datetime():
    """
    test_get_current_datetime function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.date_operations.get_current_datetime import get_current_datetime

    # Test case 1: Verify datetime structure
    mock_dt = datetime(2025, 2, 28, 14, 30, 45)
    
    with patch("functions.date_operations.get_current_datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value = mock_dt
        result = get_current_datetime()

    assert result["date"] == "2025-02-28"
    assert result["time"] == "14:30:45"
    assert result["year"] == 2025
    assert result["month"] == 2
    assert result["day"] == 28
    assert result["hour"] == 14
    assert result["minute"] == 30
    assert result["second"] == 45


def test_calculate_date_difference():
    """
    test_calculate_date_difference function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.date_operations.calculate_date_difference import calculate_date_difference

    # Test case 1: Positive difference
    result = calculate_date_difference("2025-01-10", "2025-02-28")
    
    expected = {
        "date1": "2025-01-10",
        "date2": "2025-02-28",
        "days_difference": 49,
        "absolute_days": 49,
    }
    assert result == expected

    # Test case 2: Negative difference
    result = calculate_date_difference("2025-02-28", "2025-01-10")
    assert result["days_difference"] == -49
    assert result["absolute_days"] == 49


def test_get_day_of_week():
    """
    test_get_day_of_week function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.date_operations.get_day_of_week import get_day_of_week

    # Test case 1: Friday (2025-02-28 is a Friday)
    result = get_day_of_week("2025-02-28")
    
    expected = {
        "date": "2025-02-28",
        "day_of_week": "Friday",
        "day_number": 4,
        "iso_weekday": 5,
    }
    assert result == expected

    # Test case 2: Another date
    result = get_day_of_week("2025-01-01")
    assert result["day_of_week"] == "Wednesday"


def test_get_day_of_year():
    """
    test_get_day_of_year function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.date_operations.get_day_of_year import get_day_of_year

    # Test case 1: Day 59 of 2025
    result = get_day_of_year("2025-02-28")
    
    expected = {
        "date": "2025-02-28",
        "day_of_year": 59,
        "year": 2025,
        "is_leap_year": False,
    }
    assert result == expected

    # Test case 2: Leap year check
    result = get_day_of_year("2024-12-31")
    assert result["is_leap_year"] is True
    assert result["day_of_year"] == 366


def test_add_days():
    """
    test_add_days function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.date_operations.add_days import add_days

    # Test case 1: Add positive days
    result = add_days("2025-02-28", 10)
    
    expected = {
        "original_date": "2025-02-28",
        "days_added": 10,
        "result_date": "2025-03-10",
    }
    assert result == expected

    # Test case 2: Add negative days (go backward)
    result = add_days("2025-03-15", -5)
    assert result["result_date"] == "2025-03-10"


def test_subtract_days():
    """
    test_subtract_days function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.date_operations.subtract_days import subtract_days

    # Test case 1: Subtract positive days
    result = subtract_days("2025-02-28", 10)
    
    expected = {
        "original_date": "2025-02-28",
        "days_subtracted": 10,
        "result_date": "2025-02-18",
    }
    assert result == expected

    # Test case 2: Subtract across month boundary
    result = subtract_days("2025-03-15", 20)
    assert result["result_date"] == "2025-02-23"


def test_is_leap_year():
    """
    test_is_leap_year function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.date_operations.is_leap_year import is_leap_year

    # Test case 1: Leap year (2024)
    result = is_leap_year(2024)
    
    expected = {
        "year": 2024,
        "is_leap_year": True,
        "days_in_year": 366,
    }
    assert result == expected

    # Test case 2: Non-leap year (2025)
    result = is_leap_year(2025)
    assert result["is_leap_year"] is False
    assert result["days_in_year"] == 365

    # Test case 3: Century year not divisible by 400
    result = is_leap_year(1900)
    assert result["is_leap_year"] is False

    # Test case 4: Century year divisible by 400
    result = is_leap_year(2000)
    assert result["is_leap_year"] is True

    # Test case 5: Invalid input
    with pytest.raises(ValueError):
        is_leap_year("2024")


def test_format_date():
    """
    test_format_date function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.date_operations.format_date import format_date

    # Test case 1: Default format to readable format
    result = format_date("2025-02-28")
    
    assert result["original_date"] == "2025-02-28"
    assert result["original_format"] == "%Y-%m-%d"
    assert result["formatted_date"] == "Friday, February 28, 2025"
    assert result["output_format"] == "%A, %B %d, %Y"

    # Test case 2: Custom format
    result = format_date("02/28/2025", "%m/%d/%Y", "%d-%m-%Y")
    assert result["formatted_date"] == "28-02-2025"


def test_parse_date():
    """
    test_parse_date function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.date_operations.parse_date import parse_date

    # Test case 1: Parse default format
    result = parse_date("2025-02-28")
    
    expected = {
        "input_string": "2025-02-28",
        "format": "%Y-%m-%d",
        "year": 2025,
        "month": 2,
        "day": 28,
        "iso_format": "2025-02-28",
        "weekday": "Friday",
    }
    assert result == expected

    # Test case 2: Parse custom format
    result = parse_date("28/02/2025", "%d/%m/%Y")
    assert result["year"] == 2025
    assert result["month"] == 2
    assert result["day"] == 28


if __name__ == "__main__":
    test_get_current_date()
    test_get_current_datetime()
    test_calculate_date_difference()
    test_get_day_of_week()
    test_get_day_of_year()
    test_add_days()
    test_subtract_days()
    test_is_leap_year()
    test_format_date()
    test_parse_date()
