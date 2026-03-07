from datetime import datetime


def is_valid_time(time_string: str, time_format: str = "%H:%M:%S"):
    """
    Check if a time string is valid in the given format.

    Args:
        time_string (str): Time string to validate
        time_format (str): Time format to validate against (default: %H:%M:%S)

    Returns:
        dict: Dictionary containing validation result and parsed time details if valid
    """
    try:
        parsed_time = datetime.strptime(time_string, time_format).time()
        return {
            "time_string": time_string,
            "format": time_format,
            "is_valid": True,
            "hour": parsed_time.hour,
            "minute": parsed_time.minute,
            "second": parsed_time.second,
        }
    except ValueError:
        return {
            "time_string": time_string,
            "format": time_format,
            "is_valid": False,
            "error": "Invalid time format",
        }
