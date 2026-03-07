from datetime import datetime


def timestamp_to_time(timestamp: float, format_string: str = "%H:%M:%S"):
    """
    Convert a Unix timestamp to a readable time string.

    Args:
        timestamp (float): Unix timestamp
        format_string (str): Output format string (default: %H:%M:%S)

    Returns:
        dict: Dictionary containing timestamp and formatted time details
    """
    dt = datetime.fromtimestamp(timestamp)
    time_obj = dt.time()
    formatted_time = datetime.fromtimestamp(timestamp).strftime(format_string)

    return {
        "timestamp": timestamp,
        "time": str(time_obj),
        "formatted_time": formatted_time,
        "hour": time_obj.hour,
        "minute": time_obj.minute,
        "second": time_obj.second,
        "full_datetime": dt.isoformat(),
    }
