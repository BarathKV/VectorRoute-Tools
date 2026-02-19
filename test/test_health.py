def test_calculate_bmi():
    from functions.heath.calculate_bmi import calculate_bmi
    bmi1 = calculate_bmi(170.0, 60.0)
    print(bmi1)
    assert round(bmi1, 2) == 20.76

    # bmi2 = calculate_bmi(180, 80)
    # print(bmi2)
    # assert round(bmi2, 2) == 24.69


def test_estimate_daily_calories():
    from functions.heath import estimate_daily_calories
    assert estimate_daily_calories(170, 60, 25, 'male') == 1665.0

    assert estimate_daily_calories(160, 50, 30, 'female') == 1350.0

