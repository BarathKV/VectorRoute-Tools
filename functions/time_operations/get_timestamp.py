import time


def get_timestamp():
    """
    Get the current Unix timestamp.

    Returns:
        dict: Dictionary containing current timestamp and datetime representation
    """
    current_timestamp = time.time()
    return {
        "timestamp": current_timestamp,
        "timestamp_int": int(current_timestamp),
        "milliseconds": int(current_timestamp * 1000),
    }
