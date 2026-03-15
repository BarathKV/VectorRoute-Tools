import os

DOCUMENTS_DIR = "tools/helper/documents"

def search_documents_by_title(title_query: str):
    """
    search_documents_by_title function.

    Args:
        title_query (str): Input parameter.

    Returns:
        Any: Function result.
    """
    matches = []

    for filename in os.listdir(DOCUMENTS_DIR):
        if title_query.lower() in filename.lower():
            matches.append(filename)

    return matches
