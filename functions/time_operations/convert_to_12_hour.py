from datetime import datetime


def convert_to_12_hour(time_string: str):
    """
    Convert a 24-hour format time string to 12-hour format.

    Args:
        time_string (str): Time string in 24-hour format (e.g., "14:30:00")

    Returns:
        dict: Dictionary containing original and converted times
    """
    try:
        parsed_time = datetime.strptime(time_string, "%H:%M:%S")
        time_12 = parsed_time.strftime("%I:%M:%S %p")
        return {
            "original_time": time_string,
            "original_format": "24-hour",
            "converted_time": time_12,
            "converted_format": "12-hour",
        }
    except ValueError:
        raise ValueError(f"Invalid 24-hour format: {time_string}. Expected format: HH:MM:SS")
