import math


def lcm(a: int, b: int):
    """
    Calculate the Least Common Multiple of two numbers.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        dict: Dictionary containing input numbers and LCM result
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")

    gcd_value = math.gcd(a, b)
    lcm_value = abs(a * b) // gcd_value if gcd_value != 0 else 0

    return {
        "number1": a,
        "number2": b,
        "lcm": lcm_value,
    }
