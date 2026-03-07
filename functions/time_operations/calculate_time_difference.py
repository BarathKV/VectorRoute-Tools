from datetime import datetime


def calculate_time_difference(t1: str, t2: str, time_format: str = "%H:%M:%S"):
    """
    Calculate the difference between two times.

    Args:
        t1 (str): First time as string
        t2 (str): Second time as string
        time_format (str): Time format (default: %H:%M:%S)

    Returns:
        dict: Dictionary containing time difference in hours, minutes, and seconds
    """
    parsed_t1 = datetime.strptime(t1, time_format)
    parsed_t2 = datetime.strptime(t2, time_format)

    difference = parsed_t2 - parsed_t1
    total_seconds = int(difference.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return {
        "time1": str(parsed_t1.time()),
        "time2": str(parsed_t2.time()),
        "hours_difference": hours,
        "minutes_difference": minutes,
        "seconds_difference": seconds,
        "total_seconds": total_seconds,
    }
