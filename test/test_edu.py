def test_calculate_gpa():
    from functions.edu.calculate_gpa import calculate_gpa

    # Test case 1: Basic case
    grades = [90, 80, 70]
    expected_gpa = 3.0
    assert calculate_gpa(grades) == expected_gpa

    # Test case 2: All A's
    grades = [95, 92, 88]
    expected_gpa = 4.0
    assert calculate_gpa(grades) == expected_gpa

    # Test case 3: All F's
    grades = [50, 45, 30]
    expected_gpa = 0.0
    assert calculate_gpa(grades) == expected_gpa

    # Test case 4: Mixed grades
    grades = [85, 75, 65]
    expected_gpa = 2.5
    assert calculate_gpa(grades) == expected_gpa

    # Test case 5: Empty list of grades
    grades = []
    expected_gpa = 0.0
    assert calculate_gpa(grades) == expected_gpa



def test_generate_quiz():
    from functions.edu.generate_quiz import generate_quiz

    # Test case 1: Basic case
    topic = "Math"
    quiz = generate_quiz(topic)
    assert isinstance(quiz, list)
    assert len(quiz) > 0
    for question in quiz:
        assert "question" in question
        assert "options" in question
        assert "answer" in question

    # Test case 2: Different topic
    topic = "Science"
    quiz = generate_quiz(topic)
    assert isinstance(quiz, list)
    assert len(quiz) > 0
    for question in quiz:
        assert "question" in question
        assert "options" in question
        assert "answer" in question