def test_calculate_bmi():
    from functions.heath.calculate_bmi import calculate_bmi
    bmi1 = calculate_bmi(60.0, 170.0)
    assert isinstance(bmi1, dict)
    assert isinstance(bmi1["bmi"], float)
    assert bmi1["bmi"] == 20.76
    assert bmi1["category"] == "Normal weight"

    # bmi2 = calculate_bmi(180, 80)
    # print(bmi2)
    # assert round(bmi2, 2) == 24.69


def test_estimate_daily_calories():
    from functions.heath.estimate_daily_calories import estimate_daily_calories

    male = estimate_daily_calories("male", 25, 60, 170, "sedentary")
    assert isinstance(male, dict)
    assert isinstance(male["daily_calorie_needs"], float)
    assert male["daily_calorie_needs"] == 1851.0

    female = estimate_daily_calories("female", 30, 50, 160, "sedentary")
    assert isinstance(female, dict)
    assert isinstance(female["daily_calorie_needs"], float)
    assert female["daily_calorie_needs"] == 1426.8

