import os
from datetime import datetime


def get_file_created_time(path: str):
    """
    Get the creation time of a file.

    Args:
        path (str): Path to the file

    Returns:
        dict: Dictionary containing file path and creation time
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    created_timestamp = os.path.getctime(path)
    created_datetime = datetime.fromtimestamp(created_timestamp)

    return {
        "path": path,
        "created_timestamp": created_timestamp,
        "created_datetime": created_datetime.isoformat(),
        "created_date": str(created_datetime.date()),
        "created_time": str(created_datetime.time()),
    }
