from datetime import datetime


def get_day_of_year(date: str, date_format: str = "%Y-%m-%d"):
    """
    Get the day of year (1-366) for a given date.

    Args:
        date (str): Date as string
        date_format (str): Format string for parsing date (default: %Y-%m-%d)

    Returns:
        dict: Dictionary containing day of year and whether it's a leap year
    """
    parsed_date = datetime.strptime(date, date_format).date()
    day_of_year = parsed_date.timetuple().tm_yday
    year = parsed_date.year
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    return {
        "date": str(parsed_date),
        "day_of_year": day_of_year,
        "year": year,
        "is_leap_year": is_leap,
    }
