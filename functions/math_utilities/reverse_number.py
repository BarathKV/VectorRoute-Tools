def reverse_number(n: int):
    """
    Reverse the digits of a number.

    Args:
        n (int): Integer number

    Returns:
        dict: Dictionary containing original and reversed numbers
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")

    is_negative = n < 0
    reversed_num = int(str(abs(n))[::-1])
    if is_negative:
        reversed_num = -reversed_num

    return {
        "original_number": n,
        "reversed_number": reversed_num,
    }
