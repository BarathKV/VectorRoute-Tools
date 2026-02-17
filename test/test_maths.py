def test_length_converter():
    from functions.maths.length_converter import convert_length

    assert convert_length(1, 'm', 'cm') == 100
    assert convert_length(1, 'km', 'm') == 1000
    assert convert_length(1, 'ft', 'in') == 12
    assert convert_length(1, 'yd', 'ft') == 3
    assert convert_length(1, 'mi', 'km') == 1.60934


def test_percentage_calc():
    from functions.maths.percentage_calc import calculate_percentage

    assert calculate_percentage(50, 200) == 25
    assert calculate_percentage(30, 150) == 20
    assert calculate_percentage(75, 300) == 25
    assert calculate_percentage(10, 50) == 20
    assert calculate_percentage(5, 25) == 20