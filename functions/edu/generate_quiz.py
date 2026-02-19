import requests
import html


def generate_quiz(num_questions: int, category: str = None, difficulty: str = None):
    """
    Generate a quiz using Open Trivia Database (no API key required).
    
    Args:
        num_questions: Number of questions to generate
        category: Optional category ID (e.g., 9 for General Knowledge, 18 for Science & Nature)
        difficulty: Optional difficulty level ('easy', 'medium', 'hard')
    
    Returns questions with category, difficulty, and options.
    """
    url = "https://opentdb.com/api.php"
    params = {"amount": num_questions, "type": "multiple"}
    
    if category is not None:
        params["category"] = category
    if difficulty is not None:
        params["difficulty"] = difficulty.lower()

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    quiz = []

    for item in data.get("results", []):
        options = item["incorrect_answers"] + [item["correct_answer"]]
        quiz.append(
            {
                "question": html.unescape(item["question"]),
                "category": html.unescape(item.get("category", "Unknown")),
                "difficulty": item.get("difficulty", "unknown").capitalize(),
                "options": [html.unescape(opt) for opt in options],
            }
        )

    return {"num_questions": len(quiz), "quiz": quiz}
