def calculate_bmi(height_cm: float, weight_kg: float):
    """
    Calculate Body Mass Index (BMI).
    BMI = weight (kg) / (height (m))^2
    """
    height_m = height_cm / 100

    if height_m <= 0:
        raise ValueError("Height must be greater than zero")

    bmi = weight_kg / (height_m ** 2)

    return round(bmi, 2)
