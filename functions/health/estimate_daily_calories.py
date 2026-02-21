def estimate_daily_calories(
    height_cm: float,
    weight_kg: float,
    age: int,
    gender: str,
    activity_level: str = "sedentary"
):
    """
    Estimate daily calorie needs using Mifflin–St Jeor equation.
    """

    if gender.lower() == "male":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    elif gender.lower() == "female":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    else:
        raise ValueError("Gender must be 'male' or 'female'")

    activity_factors = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9
    }

    factor = activity_factors.get(activity_level.lower())
    if factor is None:
        raise ValueError("Invalid activity level")

    calories = bmr * factor

    return round(calories, 2)
