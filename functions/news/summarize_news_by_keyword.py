import requests

from functions.news._common import build_article_summary, fetch_gnews_json, get_gnews_token


def summarize_news_by_keyword(keyword: str):
    """
    Fetch recent news articles by keyword and return a short summary.

    Args:
        keyword (str): Input parameter.

    Returns:
        Any: Function result.
    """
    token, using_demo_token = get_gnews_token()
    url = "https://gnews.io/api/v4/search"
    params = {
        "q": keyword,
        "lang": "en",
        "max": 5,
        "token": token,
    }

    try:
        data = fetch_gnews_json(url, params)
    except requests.RequestException as exc:
        return {
            "keyword": keyword,
            "articles": [],
            "error": str(exc),
        }

    summaries = []

    for article in data.get("articles", []):
        summaries.append({
            "title": article.get("title"),
            "summary": build_article_summary(article),
            "source": article.get("source", {}).get("name"),
            "published_at": article.get("publishedAt"),
        })

    result = {
        "keyword": keyword,
        "articles": summaries,
    }
    if using_demo_token:
        result["warning"] = "Using demo GNews token; results may be limited."
    return result
