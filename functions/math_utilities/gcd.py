import math


def gcd(a: int, b: int):
    """
    Calculate the Greatest Common Divisor of two numbers.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        dict: Dictionary containing input numbers and GCD result
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")

    result = math.gcd(a, b)
    return {
        "number1": a,
        "number2": b,
        "gcd": result,
    }
