def test_length_converter():
    """
    test_length_converter function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.maths.length_converter import length_converter

    assert length_converter(1, 'm', 'cm') == 100.0
    assert length_converter(1, 'km', 'm') == 1000.0
    assert round(length_converter(1, 'ft', 'in'), 5) == 12.0
    assert round(length_converter(1, 'yd', 'ft'), 5) == 3.0
    assert round(length_converter(100, 'cm', 'm'), 5) == 1.0


def test_percentage_calc():
    """
    test_percentage_calc function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    from functions.maths.percentage_calc import percentage_calc

    assert percentage_calc(50, 200) == 25.0
    assert percentage_calc(30, 150) == 20.0
    assert percentage_calc(75, 300) == 25.0
    assert percentage_calc(10, 50) == 20.0
    assert percentage_calc(5, 25) == 20.0