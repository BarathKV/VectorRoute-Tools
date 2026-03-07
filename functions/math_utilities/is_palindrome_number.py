def is_palindrome_number(n: int):
    """
    Check if a number is a palindrome.

    Args:
        n (int): Integer number

    Returns:
        dict: Dictionary containing number and palindrome status
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")

    number_str = str(abs(n))
    is_palindrome = number_str == number_str[::-1]

    return {
        "number": n,
        "is_palindrome": is_palindrome,
    }
