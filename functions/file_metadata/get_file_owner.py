import os
import stat
import pwd


def get_file_owner(path: str):
    """
    Get the owner of a file.

    Args:
        path (str): Path to the file

    Returns:
        dict: Dictionary containing file path and owner information
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    file_stat = os.stat(path)
    uid = file_stat.st_uid

    try:
        owner = pwd.getpwuid(uid).pw_name
    except (KeyError, AttributeError):
        owner = f"UID {uid}"

    return {
        "path": path,
        "uid": uid,
        "owner": owner,
    }
