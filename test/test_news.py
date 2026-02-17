def test_get_latest_headlines():
    from functions.news.get_latest_headlines import get_latest_headlines
    
    # Test with a valid country code
    result = get_latest_headlines("us")
    assert "country" in result
    assert result["country"] == "us"
    assert "headlines" in result
    assert isinstance(result["headlines"], list)
    assert len(result["headlines"]) > 0
    
    # Test with an invalid country code
    try:
        get_latest_headlines("invalid_code")
        assert False, "Expected an exception for invalid country code"
    except Exception as e:
        assert str(e) == "Failed to fetch news: 400 Bad Request"


def test_get_trending_topics():
    from functions.news.get_trending_topics import get_trending_topics
    
    result = get_trending_topics()
    assert "trending_topics" in result
    assert isinstance(result["trending_topics"], list)
    assert len(result["trending_topics"]) > 0



def test_summarize_news_by_keyword():
    from functions.news.summarize_news_by_keyword import summarize_news_by_keyword
    
    # Test with a common keyword
    result = summarize_news_by_keyword("technology")
    assert "keyword" in result
    assert result["keyword"] == "technology"
    assert "summary" in result
    assert isinstance(result["summary"], str)
    assert len(result["summary"]) > 0
    
    # Test with a keyword that may not yield results
    result = summarize_news_by_keyword("economy")
    assert "keyword" in result
    assert result["keyword"] == "economy"
    assert "summary" in result
    assert isinstance(result["summary"], str)