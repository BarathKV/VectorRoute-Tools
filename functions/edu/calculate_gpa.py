def calculate_gpa(grades: list, credits: list):
    """
    Calculate GPA using weighted average method.

    Args:
        grades (list): Input parameter.
        credits (list): Input parameter.

    Returns:
        Any: Function result.
    """
    if len(grades) != len(credits):
        raise ValueError("Grades and credits must be of the same length")

    total_points = 0
    total_credits = 0

    for grade, credit in zip(grades, credits):
        total_points += grade * credit
        total_credits += credit

    if total_credits == 0:
        raise ValueError("Total credits cannot be zero")

    gpa = total_points / total_credits

    return {
        "grades": grades,
        "credits": credits,
        "gpa": round(gpa, 2)
    }
