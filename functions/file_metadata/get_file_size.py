import os


def get_file_size(path: str):
    """
    Get the size of a file in bytes.

    Args:
        path (str): Path to the file

    Returns:
        dict: Dictionary containing file path and size in bytes
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    if not os.path.isfile(path):
        raise ValueError(f"Path is not a file: {path}")

    size_bytes = os.path.getsize(path)
    return {
        "path": path,
        "size_bytes": size_bytes,
        "size_kb": round(size_bytes / 1024, 2),
        "size_mb": round(size_bytes / (1024 * 1024), 2),
    }
