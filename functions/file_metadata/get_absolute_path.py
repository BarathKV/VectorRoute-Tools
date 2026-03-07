import os


def get_absolute_path(path: str):
    """
    Get the absolute path of a file or directory.

    Args:
        path (str): Relative or absolute path

    Returns:
        dict: Dictionary containing original and absolute paths
    """
    absolute_path = os.path.abspath(path)

    return {
        "original_path": path,
        "absolute_path": absolute_path,
        "exists": os.path.exists(absolute_path),
    }
