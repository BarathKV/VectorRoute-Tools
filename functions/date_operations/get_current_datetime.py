from datetime import datetime


def get_current_datetime():
    """
    Get current date and time with timestamp details.

    Args:
        None

    Returns:
        Any: Function result.
    """
    now = datetime.now()
    return {
        "datetime": now.isoformat(),
        "date": str(now.date()),
        "time": str(now.time()),
        "timestamp": now.timestamp(),
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second,
    }
