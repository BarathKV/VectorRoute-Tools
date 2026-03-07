from datetime import datetime


def get_current_time():
    """
    Get the current time in HH:MM:SS format.

    Returns:
        dict: Dictionary containing current time and time component details
    """
    now = datetime.now().time()
    return {
        "time": str(now),
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second,
        "microsecond": now.microsecond,
    }
