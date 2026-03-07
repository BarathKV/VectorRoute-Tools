def is_leap_year(year: int):
    """
    Check if a given year is a leap year.

    Args:
        year (int): Year to check

    Returns:
        dict: Dictionary containing year and leap year status
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer")

    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    return {
        "year": year,
        "is_leap_year": is_leap,
        "days_in_year": 366 if is_leap else 365,
    }
