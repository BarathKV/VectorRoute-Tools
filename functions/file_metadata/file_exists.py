import os


def file_exists(path: str):
    """
    Check if a file or directory exists.

    Args:
        path (str): Path to check

    Returns:
        dict: Dictionary containing path and existence status
    """
    exists = os.path.exists(path)
    is_file = os.path.isfile(path) if exists else False
    is_dir = os.path.isdir(path) if exists else False

    return {
        "path": path,
        "exists": exists,
        "is_file": is_file,
        "is_directory": is_dir,
    }
