from datetime import datetime


def get_current_date():
    """
    Get today's date in YYYY-MM-DD format.

    Args:
        None

    Returns:
        Any: Function result.
    """
    today = datetime.now().date()
    return {
        "date": str(today),
        "year": today.year,
        "month": today.month,
        "day": today.day,
    }
