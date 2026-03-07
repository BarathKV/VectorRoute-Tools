def fibonacci(n: int):
    """
    Get the nth number in the Fibonacci sequence (0-indexed).

    Args:
        n (int): Position in Fibonacci sequence (non-negative)

    Returns:
        dict: Dictionary containing position and Fibonacci number
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    if n == 0:
        fib_num = 0
    elif n == 1:
        fib_num = 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        fib_num = b

    return {
        "position": n,
        "fibonacci_number": fib_num,
    }
