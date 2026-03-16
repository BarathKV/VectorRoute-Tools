import requests

from functions.news._common import GNEWS_TOPICS, fetch_gnews_json, get_gnews_token, normalize_category


def get_latest_headlines(category: str):
    """
    Get latest news headlines by category using GNews public API.

    Args:
        category (str): Input parameter.

    Returns:
        Any: Function result.
    """
    normalized_category = normalize_category(category)
    if not normalized_category:
        return {
            "category": category,
            "headlines": [],
            "error": f"Unsupported category: {category}",
            "supported_categories": sorted(GNEWS_TOPICS),
        }

    token, using_demo_token = get_gnews_token()
    url = "https://gnews.io/api/v4/top-headlines"
    params = {
        "topic": normalized_category,
        "lang": "en",
        "max": 5,
        "token": token,
    }

    try:
        data = fetch_gnews_json(url, params)
    except requests.RequestException as exc:
        return {
            "category": category,
            "headlines": [],
            "error": str(exc),
        }

    headlines = []
    for article in data.get("articles", []):
        headlines.append({
            "title": article.get("title"),
            "source": article.get("source", {}).get("name"),
            "published_at": article.get("publishedAt"),
        })

    result = {
        "category": category,
        "resolved_category": normalized_category,
        "headlines": headlines,
    }
    if using_demo_token:
        result["warning"] = "Using demo GNews token; results may be limited."
    return result
