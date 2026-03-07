def power(base: float, exponent: float):
    """
    Calculate base raised to the power of exponent.

    Args:
        base (float): Base number
        exponent (float): Exponent

    Returns:
        dict: Dictionary containing base, exponent, and result
    """
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise ValueError("Both inputs must be numbers")

    result = base ** exponent

    return {
        "base": base,
        "exponent": exponent,
        "result": result,
    }
