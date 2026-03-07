def sum_of_digits(n: int):
    """
    Calculate the sum of digits in a number.

    Args:
        n (int): Integer number (positive or negative)

    Returns:
        dict: Dictionary containing number and sum of its digits
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")

    digit_sum = sum(int(digit) for digit in str(abs(n)))

    return {
        "number": n,
        "sum_of_digits": digit_sum,
    }
