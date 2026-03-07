from datetime import datetime


def convert_time_format(time_string: str, input_format: str = "%H:%M:%S", output_format: str = "%I:%M:%S %p"):
    """
    Convert a time string from one format to another.

    Args:
        time_string (str): Time as string
        input_format (str): Input time format (default: %H:%M:%S)
        output_format (str): Output time format (default: %I:%M:%S %p)

    Returns:
        dict: Dictionary containing original and converted time strings
    """
    parsed_time = datetime.strptime(time_string, input_format)
    converted_time = parsed_time.strftime(output_format)

    return {
        "original_time": time_string,
        "input_format": input_format,
        "converted_time": converted_time,
        "output_format": output_format,
    }
