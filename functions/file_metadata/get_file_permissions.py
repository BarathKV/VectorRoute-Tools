import os
import stat


def get_file_permissions(path: str):
    """
    Get the permissions of a file in both octal and symbolic notation.

    Args:
        path (str): Path to the file

    Returns:
        dict: Dictionary containing file path and permission details
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    file_stat = os.stat(path)
    mode = file_stat.st_mode

    # Octal permissions
    octal_perms = oct(stat.S_IMODE(mode))

    # Symbolic permissions
    permissions = stat.filemode(mode)

    return {
        "path": path,
        "octal": octal_perms,
        "symbolic": permissions,
        "owner_read": bool(mode & stat.S_IRUSR),
        "owner_write": bool(mode & stat.S_IWUSR),
        "owner_execute": bool(mode & stat.S_IXUSR),
    }
