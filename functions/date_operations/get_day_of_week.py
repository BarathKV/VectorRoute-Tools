from datetime import datetime


def get_day_of_week(date: str, date_format: str = "%Y-%m-%d"):
    """
    Get the day of week for a given date.

    Args:
        date (str): Date as string
        date_format (str): Format string for parsing date (default: %Y-%m-%d)

    Returns:
        dict: Dictionary containing day of week name and number
    """
    parsed_date = datetime.strptime(date, date_format).date()
    day_num = parsed_date.weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    return {
        "date": str(parsed_date),
        "day_of_week": days[day_num],
        "day_number": day_num,
        "iso_weekday": parsed_date.isoweekday(),
    }
