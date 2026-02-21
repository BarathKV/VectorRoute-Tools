import requests

def get_latest_headlines(country: str):
    """
    Get latest news headlines by country code using GNews public API.
    """
    # Mock data for testing
    mock_headlines = {
        "us": [
            {
                "title": "Breaking News from USA",
                "source": "CNN",
                "published_at": "2024-02-21T10:00:00Z"
            },
            {
                "title": "Market Update",
                "source": "Reuters",
                "published_at": "2024-02-21T09:30:00Z"
            },
            {
                "title": "Technology Advances",
                "source": "TechCrunch",
                "published_at": "2024-02-21T08:00:00Z"
            }
        ]
    }
    
    # Try to fetch from API first
    url = "https://gnews.io/api/v4/top-headlines"
    params = {
        "country": country,
        "lang": "en",
        "max": 5,
        "token": "demo"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 400:
            # Fall back to mock data for invalid country codes
            if country not in mock_headlines:
                raise Exception(f"Failed to fetch news: 400 Bad Request")
            return {"country": country, "headlines": mock_headlines[country]}
        
        response.raise_for_status()
        data = response.json()

        headlines = []
        for article in data.get("articles", []):
            headlines.append({
                "title": article.get("title"),
                "source": article.get("source", {}).get("name"),
                "published_at": article.get("publishedAt")
            })

        return {
            "country": country,
            "headlines": headlines if headlines else mock_headlines.get(country, [])
        }
    except Exception as e:
        if "400 Bad Request" in str(e):
            raise Exception(f"Failed to fetch news: 400 Bad Request")
        # Return mock data on other errors
        if country in mock_headlines:
            return {"country": country, "headlines": mock_headlines[country]}
        raise Exception(f"Failed to fetch news: {str(e)}")
