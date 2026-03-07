from datetime import datetime


def get_current_date():
    """
    Get today's date in YYYY-MM-DD format.

    Returns:
        dict: Dictionary containing current date string and date object details
    """
    today = datetime.now().date()
    return {
        "date": str(today),
        "year": today.year,
        "month": today.month,
        "day": today.day,
    }
