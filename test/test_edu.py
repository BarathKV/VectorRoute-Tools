import pytest
import sys
from pathlib import Path

# Add parent directory to path so we can import functions
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_calculate_gpa():
    from functions.edu.calculate_gpa import calculate_gpa

    # Test case 1: Basic case
    grades = [9.56, 8.75, 7.80]
    credits = [21, 20, 23]
    expected_gpa = 8.67

    assert calculate_gpa(grades, credits)["gpa"] == expected_gpa

    # Test case 2: Different grades and credits
    grades = [8.00, 7.50, 9.00]
    credits = [20, 22, 18]
    expected_gpa = 8.12

    assert calculate_gpa(grades, credits)["gpa"] == expected_gpa


    # Test case 3: Empty lists
    grades = []
    credits = []
    expected_gpa = 0.0
    
    with pytest.raises(ValueError):
        calculate_gpa(grades, credits)



def test_generate_quiz():
    from functions.edu.generate_quiz import generate_quiz

    # Test case 1: Basic case with difficulty parameter
    quiz = generate_quiz(5, difficulty="easy")
    print(quiz,len(quiz["quiz"]))
    assert "quiz" in quiz
    assert len(quiz["quiz"]) > 0
    for question in quiz["quiz"]:
        assert "question" in question
        assert "options" in question
        assert "category" in question
        assert "difficulty" in question


if __name__ == "__main__":
    test_calculate_gpa()
    test_generate_quiz()