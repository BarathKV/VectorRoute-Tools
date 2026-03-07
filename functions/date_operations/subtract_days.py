from datetime import datetime, timedelta


def subtract_days(date: str, n: int, date_format: str = "%Y-%m-%d"):
    """
    Subtract N days from a given date.

    Args:
        date (str): Date as string
        n (int): Number of days to subtract
        date_format (str): Format string for parsing date (default: %Y-%m-%d)

    Returns:
        dict: Dictionary containing original and resulting dates
    """
    parsed_date = datetime.strptime(date, date_format).date()
    result_date = parsed_date - timedelta(days=n)

    return {
        "original_date": str(parsed_date),
        "days_subtracted": n,
        "result_date": str(result_date),
    }
