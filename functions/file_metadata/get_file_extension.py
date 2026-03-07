import os


def get_file_extension(path: str):
    """
    Get the file extension from a file path.

    Args:
        path (str): Path to the file

    Returns:
        dict: Dictionary containing file name and extension
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    filename = os.path.basename(path)
    name, extension = os.path.splitext(filename)

    return {
        "path": path,
        "filename": filename,
        "name": name,
        "extension": extension if extension else "No extension",
    }
