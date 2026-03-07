import os


def is_file_readable(path: str):
    """
    Check if a file is readable.

    Args:
        path (str): Path to the file

    Returns:
        dict: Dictionary containing file path and readable status
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    is_readable = os.access(path, os.R_OK)

    return {
        "path": path,
        "is_readable": is_readable,
    }
