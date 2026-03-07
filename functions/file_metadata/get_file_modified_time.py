import os
from datetime import datetime


def get_file_modified_time(path: str):
    """
    Get the modification time of a file.

    Args:
        path (str): Path to the file

    Returns:
        dict: Dictionary containing file path and modification time
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    modified_timestamp = os.path.getmtime(path)
    modified_datetime = datetime.fromtimestamp(modified_timestamp)

    return {
        "path": path,
        "modified_timestamp": modified_timestamp,
        "modified_datetime": modified_datetime.isoformat(),
        "modified_date": str(modified_datetime.date()),
        "modified_time": str(modified_datetime.time()),
    }
