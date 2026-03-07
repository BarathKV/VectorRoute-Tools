from unittest.mock import Mock, patch


def test_get_latest_headlines():
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
    assert "headlines" in result
    assert isinstance(result["headlines"], list)
    assert len(result["headlines"]) > 0
    assert isinstance(result["headlines"][0], dict)


def test_get_trending_topics():
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



def test_summarize_news_by_keyword():
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