def is_prime(n: int):
    """
    Check if a number is prime.

    Args:
        n (int): Integer to check

    Returns:
        dict: Dictionary containing number and prime status
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")

    if n < 2:
        return {
            "number": n,
            "is_prime": False,
        }

    is_prime_flag = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime_flag = False
            break

    return {
        "number": n,
        "is_prime": is_prime_flag,
    }
