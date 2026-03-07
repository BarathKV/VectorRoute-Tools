from datetime import datetime


def convert_to_24_hour(time_string: str):
    """
    Convert a 12-hour format time string to 24-hour format.

    Args:
        time_string (str): Time string in 12-hour format (e.g., "02:30:00 PM")

    Returns:
        dict: Dictionary containing original and converted times
    """
    try:
        parsed_time = datetime.strptime(time_string, "%I:%M:%S %p")
        time_24 = parsed_time.strftime("%H:%M:%S")
        return {
            "original_time": time_string,
            "original_format": "12-hour",
            "converted_time": time_24,
            "converted_format": "24-hour",
        }
    except ValueError:
        raise ValueError(f"Invalid 12-hour format: {time_string}. Expected format: HH:MM:SS AM/PM")
