import os


def is_file_writable(path: str):
    """
    Check if a file is writable.

    Args:
        path (str): Path to the file

    Returns:
        dict: Dictionary containing file path and writable status
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    is_writable = os.access(path, os.W_OK)

    return {
        "path": path,
        "is_writable": is_writable,
    }
