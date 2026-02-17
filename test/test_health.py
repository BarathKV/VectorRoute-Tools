def tset_caculate_bmi():
    from functions.heath import caculate_bmi
    assert caculate_bmi(170, 60) == 20.76

    assert caculate_bmi(180, 80) == 24.69


def test_estimate_daily_calories():
    from functions.heath import estimate_daily_calories
    assert estimate_daily_calories(170, 60, 25, 'male') == 1665.0

    assert estimate_daily_calories(160, 50, 30, 'female') == 1350.0

