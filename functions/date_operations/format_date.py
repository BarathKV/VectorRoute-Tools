from datetime import datetime


def format_date(date: str, input_format: str = "%Y-%m-%d", output_format: str = "%A, %B %d, %Y"):
    """
    Format a date string from one format to another.

    Args:
        date (str): Date as string
        input_format (str): Input date format (default: %Y-%m-%d)
        output_format (str): Output date format (default: %A, %B %d, %Y)

    Returns:
        dict: Dictionary containing original date and formatted date string
    """
    parsed_date = datetime.strptime(date, input_format)
    formatted_date = parsed_date.strftime(output_format)

    return {
        "original_date": str(parsed_date.date()),
        "original_format": input_format,
        "formatted_date": formatted_date,
        "output_format": output_format,
    }
