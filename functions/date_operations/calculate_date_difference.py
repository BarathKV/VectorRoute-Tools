from datetime import datetime


def calculate_date_difference(date1: str, date2: str, date_format: str = "%Y-%m-%d"):
    """
    Calculate the difference between two dates.

    Args:
        date1 (str): First date as string
        date2 (str): Second date as string
        date_format (str): Format string for parsing dates (default: %Y-%m-%d)

    Returns:
        dict: Dictionary containing days difference and absolute difference
    """
    parsed_date1 = datetime.strptime(date1, date_format).date()
    parsed_date2 = datetime.strptime(date2, date_format).date()

    difference = parsed_date2 - parsed_date1
    days_diff = difference.days

    return {
        "date1": str(parsed_date1),
        "date2": str(parsed_date2),
        "days_difference": days_diff,
        "absolute_days": abs(days_diff),
    }
