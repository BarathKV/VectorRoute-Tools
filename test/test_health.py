def test_calculate_bmi():
    from functions.health.calculate_bmi import calculate_bmi
    bmi1 = calculate_bmi(170.0, 60.0)
    print(bmi1)
    assert round(bmi1, 2) == 20.76

    # bmi2 = calculate_bmi(180, 80)
    # print(bmi2)
    # assert round(bmi2, 2) == 24.69


def test_estimate_daily_calories():
    from functions.health.estimate_daily_calories import estimate_daily_calories
    result1 = estimate_daily_calories(170, 60, 25, 'male')
    print(f"Test 1 (male): {result1}")
    assert result1 == 1851.0

    result2 = estimate_daily_calories(160, 50, 30, 'female')
    print(f"Test 2 (female): {result2}")
    assert result2 == 1426.8

