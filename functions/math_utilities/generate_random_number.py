import random


def generate_random_number(min_val: int, max_val: int):
    """
    Generate a random integer between min and max (inclusive).

    Args:
        min_val (int): Minimum value (inclusive)
        max_val (int): Maximum value (inclusive)

    Returns:
        dict: Dictionary containing range and generated random number
    """
    if not isinstance(min_val, int) or not isinstance(max_val, int):
        raise ValueError("Both inputs must be integers")

    if min_val > max_val:
        raise ValueError("min_val must be less than or equal to max_val")

    random_num = random.randint(min_val, max_val)

    return {
        "min": min_val,
        "max": max_val,
        "random_number": random_num,
    }
