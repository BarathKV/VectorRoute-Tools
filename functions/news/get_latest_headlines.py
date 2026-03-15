import requests


def get_latest_headlines(category: str):
    """
    Get latest news headlines by category using GNews public API.

    Args:
        category (str): Input parameter.

    Returns:
        Any: Function result.
    """
    url = "https://gnews.io/api/v4/top-headlines"
    params = {
        "topic": category,
        "lang": "en",
        "max": 5,
        "token": "demo"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as exc:
        return {
            "category": category,
            "headlines": [],
            "error": str(exc)
        }

    headlines = []
    for article in data.get("articles", []):
        headlines.append({
            "title": article.get("title"),
            "source": article.get("source", {}).get("name"),
            "published_at": article.get("publishedAt")
        })

    return {
        "category": category,
        "headlines": headlines
    }
