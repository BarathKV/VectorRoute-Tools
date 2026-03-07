import pytest
import sys
from pathlib import Path
from unittest.mock import Mock, patch

# Add parent directory to path so we can import functions
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_factorial():
    from functions.math_utilities.factorial import factorial

    # Test case 1: Calculate factorial of 5
    result = factorial(5)
    expected = {
        "number": 5,
        "factorial": 120,
    }
    assert result == expected

    # Test case 2: Factorial of 0
    result = factorial(0)
    assert result["factorial"] == 1

    # Test case 3: Invalid input
    with pytest.raises(ValueError):
        factorial(-1)


def test_is_prime():
    from functions.math_utilities.is_prime import is_prime

    # Test case 1: Prime number
    result = is_prime(17)
    expected = {
        "number": 17,
        "is_prime": True,
    }
    assert result == expected

    # Test case 2: Not prime
    result = is_prime(4)
    assert result["is_prime"] is False

    # Test case 3: Edge case - 2 is prime
    result = is_prime(2)
    assert result["is_prime"] is True

    # Test case 4: Numbers less than 2
    result = is_prime(1)
    assert result["is_prime"] is False


def test_gcd():
    from functions.math_utilities.gcd import gcd

    # Test case 1: GCD of 48 and 18
    result = gcd(48, 18)
    expected = {
        "number1": 48,
        "number2": 18,
        "gcd": 6,
    }
    assert result == expected

    # Test case 2: GCD of coprime numbers
    result = gcd(17, 19)
    assert result["gcd"] == 1


def test_lcm():
    from functions.math_utilities.lcm import lcm

    # Test case 1: LCM of 12 and 18
    result = lcm(12, 18)
    expected = {
        "number1": 12,
        "number2": 18,
        "lcm": 36,
    }
    assert result == expected

    # Test case 2: LCM of same numbers
    result = lcm(5, 5)
    assert result["lcm"] == 5


def test_fibonacci():
    from functions.math_utilities.fibonacci import fibonacci

    # Test case 1: Fibonacci at position 6 (0, 1, 1, 2, 3, 5, 8)
    result = fibonacci(6)
    expected = {
        "position": 6,
        "fibonacci_number": 8,
    }
    assert result == expected

    # Test case 2: Fibonacci at position 0
    result = fibonacci(0)
    assert result["fibonacci_number"] == 0

    # Test case 3: Fibonacci at position 1
    result = fibonacci(1)
    assert result["fibonacci_number"] == 1

    # Test case 4: Invalid input
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_sum_of_digits():
    from functions.math_utilities.sum_of_digits import sum_of_digits

    # Test case 1: Sum of digits in 12345
    result = sum_of_digits(12345)
    expected = {
        "number": 12345,
        "sum_of_digits": 15,
    }
    assert result == expected

    # Test case 2: Negative number
    result = sum_of_digits(-123)
    assert result["sum_of_digits"] == 6

    # Test case 3: Single digit
    result = sum_of_digits(7)
    assert result["sum_of_digits"] == 7


def test_reverse_number():
    from functions.math_utilities.reverse_number import reverse_number

    # Test case 1: Reverse 12345
    result = reverse_number(12345)
    expected = {
        "original_number": 12345,
        "reversed_number": 54321,
    }
    assert result == expected

    # Test case 2: Reverse negative number
    result = reverse_number(-123)
    assert result["reversed_number"] == -321

    # Test case 3: Single digit
    result = reverse_number(7)
    assert result["reversed_number"] == 7


def test_is_palindrome_number():
    from functions.math_utilities.is_palindrome_number import is_palindrome_number

    # Test case 1: Palindrome number
    result = is_palindrome_number(12321)
    expected = {
        "number": 12321,
        "is_palindrome": True,
    }
    assert result == expected

    # Test case 2: Not a palindrome
    result = is_palindrome_number(123)
    assert result["is_palindrome"] is False

    # Test case 3: Single digit is palindrome
    result = is_palindrome_number(5)
    assert result["is_palindrome"] is True

    # Test case 4: Negative palindrome
    result = is_palindrome_number(-121)
    assert result["is_palindrome"] is True


def test_power():
    from functions.math_utilities.power import power

    # Test case 1: 2 to power 8
    result = power(2, 8)
    expected = {
        "base": 2,
        "exponent": 8,
        "result": 256,
    }
    assert result == expected

    # Test case 2: 5 to power 3
    result = power(5, 3)
    assert result["result"] == 125

    # Test case 3: Any number to power 0
    result = power(100, 0)
    assert result["result"] == 1

    # Test case 4: Negative exponent
    result = power(2, -2)
    assert result["result"] == 0.25


def test_generate_random_number():
    from functions.math_utilities.generate_random_number import generate_random_number

    # Test case 1: Generate random between 1 and 100
    with patch("functions.math_utilities.generate_random_number.random") as mock_random:
        mock_random.randint.return_value = 42
        result = generate_random_number(1, 100)

    expected = {
        "min": 1,
        "max": 100,
        "random_number": 42,
    }
    assert result == expected

    # Test case 2: Verify random is within range (multiple calls)
    for _ in range(10):
        result = generate_random_number(10, 20)
        assert 10 <= result["random_number"] <= 20

    # Test case 3: Invalid range
    with pytest.raises(ValueError):
        generate_random_number(100, 10)


if __name__ == "__main__":
    test_factorial()
    test_is_prime()
    test_gcd()
    test_lcm()
    test_fibonacci()
    test_sum_of_digits()
    test_reverse_number()
    test_is_palindrome_number()
    test_power()
    test_generate_random_number()
