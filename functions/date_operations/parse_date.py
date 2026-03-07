from datetime import datetime


def parse_date(date_string: str, format_string: str = "%Y-%m-%d"):
    """
    Parse a date string and return date components.

    Args:
        date_string (str): Date string to parse
        format_string (str): Format string for parsing (default: %Y-%m-%d)

    Returns:
        dict: Dictionary containing parsed date components
    """
    parsed_date = datetime.strptime(date_string, format_string).date()

    return {
        "input_string": date_string,
        "format": format_string,
        "year": parsed_date.year,
        "month": parsed_date.month,
        "day": parsed_date.day,
        "iso_format": str(parsed_date),
        "weekday": parsed_date.strftime("%A"),
    }
