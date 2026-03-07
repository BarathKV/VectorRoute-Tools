from datetime import datetime, timedelta


def add_hours(time_string: str, hours: int, time_format: str = "%H:%M:%S"):
    """
    Add hours to a given time.

    Args:
        time_string (str): Time as string
        hours (int): Number of hours to add
        time_format (str): Time format (default: %H:%M:%S)

    Returns:
        dict: Dictionary containing original and resulting times
    """
    parsed_time = datetime.strptime(time_string, time_format)
    result_time = parsed_time + timedelta(hours=hours)

    return {
        "original_time": time_string,
        "hours_added": hours,
        "result_time": result_time.strftime(time_format),
        "result_datetime": result_time.isoformat(),
    }
