import math


def factorial(n: int):
    """
    Calculate the factorial of a number.

    Args:
        n (int): Non-negative integer

    Returns:
        dict: Dictionary containing input number and factorial result
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    result = math.factorial(n)
    return {
        "number": n,
        "factorial": result,
    }
