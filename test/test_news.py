import os
from unittest.mock import Mock, patch


def test_get_latest_headlines():
    """
    test_get_latest_headlines function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.news.get_latest_headlines import get_latest_headlines

    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "articles": [
            {
                "title": "Market updates",
                "source": {"name": "Example News"},
                "publishedAt": "2026-03-07T10:00:00Z"
            }
        ]
    }

    with patch("functions.news.get_latest_headlines.requests.get", return_value=mock_response):
        result = get_latest_headlines("business")

    assert "category" in result
    assert result["category"] == "business"
    assert result["resolved_category"] == "business"
    assert "headlines" in result
    assert isinstance(result["headlines"], list)
    assert len(result["headlines"]) > 0
    assert isinstance(result["headlines"][0], dict)
    assert "warning" in result


def test_get_latest_headlines_maps_category_and_uses_env_token():
    from functions.news.get_latest_headlines import get_latest_headlines

    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"articles": []}

    with patch.dict(os.environ, {"GNEWS_API_TOKEN": "secret-token"}, clear=False):
        with patch("functions.news._common.requests.get", return_value=mock_response) as mock_get:
            result = get_latest_headlines("finance")

    assert result["resolved_category"] == "business"
    assert "warning" not in result
    assert mock_get.call_args.kwargs["params"]["token"] == "secret-token"
    assert mock_get.call_args.kwargs["params"]["topic"] == "business"


def test_get_latest_headlines_rejects_unsupported_category():
    from functions.news.get_latest_headlines import get_latest_headlines

    result = get_latest_headlines("crypto")

    assert result["category"] == "crypto"
    assert result["headlines"] == []
    assert "error" in result
    assert "supported_categories" in result


def test_get_trending_topics():
    """
    test_get_trending_topics function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.news.get_trending_topics import get_trending_topics

    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "articles": [
            {"title": "Global markets rally strongly"},
            {"title": "Markets outlook remains positive"},
            {"title": "Technology sector expands rapidly"},
        ]
    }

    with patch("functions.news.get_trending_topics.requests.get", return_value=mock_response):
        result = get_trending_topics()

    assert "trending_topics" in result
    assert isinstance(result["trending_topics"], list)
    assert len(result["trending_topics"]) > 0
    assert isinstance(result["trending_topics"][0]["topic"], str)
    assert isinstance(result["trending_topics"][0]["count"], int)
    assert result["trending_topics"][0]["topic"] == "markets"
    assert result["trending_topics"][0]["count"] == 2


def test_get_trending_topics_prefers_repeated_phrases():
    from functions.news.get_trending_topics import get_trending_topics

    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "articles": [
            {"title": "AI market surges as chip demand jumps"},
            {"title": "AI market expands as enterprise demand rises"},
            {"title": "Cloud spending climbs while AI market matures"},
        ]
    }

    with patch("functions.news._common.requests.get", return_value=mock_response):
        result = get_trending_topics()

    assert result["trending_topics"][0]["topic"] == "ai market"
    assert result["trending_topics"][0]["count"] == 3



def test_summarize_news_by_keyword():
    """
    test_summarize_news_by_keyword function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.news.summarize_news_by_keyword import summarize_news_by_keyword

    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "articles": [
            {
                "title": "Technology adoption rises",
                "description": "New AI tools improve workflows across teams."
            }
        ]
    }

    with patch("functions.news.summarize_news_by_keyword.requests.get", return_value=mock_response):
        result = summarize_news_by_keyword("technology")

    assert "keyword" in result
    assert result["keyword"] == "technology"
    assert "articles" in result
    assert isinstance(result["articles"], list)
    assert len(result["articles"]) == 1
    assert isinstance(result["articles"][0]["summary"], str)
    assert result["articles"][0]["source"] is None


def test_summarize_news_by_keyword_falls_back_to_content_and_trims_summary():
    from functions.news.summarize_news_by_keyword import summarize_news_by_keyword

    long_content = (
        "Artificial intelligence is reshaping software delivery across teams. "
        "Companies are using AI copilots to automate repetitive coding tasks. "
        "Leaders are also revisiting governance, security, and quality controls. "
        "This extra sentence should be trimmed from the final summary output."
    )

    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "articles": [
            {
                "title": "AI adoption rises",
                "description": "",
                "content": long_content,
                "source": {"name": "Example News"},
                "publishedAt": "2026-03-16T08:00:00Z",
            }
        ]
    }

    with patch("functions.news._common.requests.get", return_value=mock_response):
        result = summarize_news_by_keyword("AI")

    assert result["articles"][0]["summary"].endswith(".")
    assert len(result["articles"][0]["summary"]) <= 240
    assert result["articles"][0]["source"] == "Example News"
    assert result["articles"][0]["published_at"] == "2026-03-16T08:00:00Z"
