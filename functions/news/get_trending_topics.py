import requests

from functions.news._common import extract_trending_topics, fetch_gnews_json, get_gnews_token


def get_trending_topics():
    """
    Get trending news topics based on keyword frequency

    Args:
        None

    Returns:
        Any: Function result.
    """
    token, using_demo_token = get_gnews_token()
    url = "https://gnews.io/api/v4/top-headlines"
    params = {
        "lang": "en",
        "max": 10,
        "token": token,
    }

    try:
        data = fetch_gnews_json(url, params)
    except requests.RequestException as exc:
        return {
            "trending_topics": [],
            "error": str(exc),
        }

    result = {
        "trending_topics": extract_trending_topics(data.get("articles", []), limit=5),
    }
    if using_demo_token:
        result["warning"] = "Using demo GNews token; results may be limited."
    return result
