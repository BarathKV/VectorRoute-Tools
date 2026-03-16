import os
import re
from collections import Counter

import requests


GNEWS_TOPICS = {
    "world": "world",
    "nation": "nation",
    "business": "business",
    "technology": "technology",
    "entertainment": "entertainment",
    "sports": "sports",
    "science": "science",
    "health": "health",
    "politics": "nation",
    "finance": "business",
}

STOPWORDS = {
    "about",
    "after",
    "amid",
    "among",
    "and",
    "are",
    "because",
    "before",
    "being",
    "breaking",
    "could",
    "from",
    "into",
    "latest",
    "live",
    "more",
    "news",
    "over",
    "report",
    "reports",
    "says",
    "than",
    "that",
    "their",
    "there",
    "these",
    "they",
    "this",
    "today",
    "update",
    "updates",
    "what",
    "when",
    "where",
    "which",
    "with",
}


def get_gnews_token():
    token = os.getenv("GNEWS_API_TOKEN", "").strip()
    if token:
        return token, False
    return "demo", True


def fetch_gnews_json(url, params):
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def normalize_category(category):
    normalized = (category or "").strip().lower()
    return GNEWS_TOPICS.get(normalized)


def extract_trending_topics(articles, limit=5):
    unigram_counts = Counter()
    bigram_counts = Counter()

    for article in articles:
        title = article.get("title") or ""
        tokens = [
            token
            for token in re.findall(r"[A-Za-z0-9']+", title.lower())
            if len(token) > 1 and token not in STOPWORDS
        ]
        if not tokens:
            continue

        unique_tokens = set(tokens)
        unigram_counts.update(unique_tokens)

        unique_bigrams = {
            f"{tokens[i]} {tokens[i + 1]}"
            for i in range(len(tokens) - 1)
            if tokens[i] != tokens[i + 1]
        }
        bigram_counts.update(unique_bigrams)

    topics = []
    for phrase, count in bigram_counts.most_common():
        if count > 1:
            topics.append({"topic": phrase, "count": count})
        if len(topics) >= limit:
            return topics

    for word, count in unigram_counts.most_common():
        if any(word in item["topic"].split() for item in topics):
            continue
        topics.append({"topic": word, "count": count})
        if len(topics) >= limit:
            break

    return topics


def build_article_summary(article, max_length=240):
    for field in ("description", "content", "title"):
        value = article.get(field)
        if value:
            text = " ".join(str(value).split())
            if len(text) <= max_length:
                return text

            sentence_end = text.rfind(". ", 0, max_length + 1)
            if sentence_end > 40:
                return text[: sentence_end + 1]
            return text[:max_length].rstrip() + "..."

    return ""
