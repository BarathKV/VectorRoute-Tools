def convert_length(value:float, from_unit:str, to_unit:str) -> float:
    # Define conversion factors (in meters)
    conversion_factors = {
        'm': 1.0,
        'metre': 1.0,
        'km': 1000.0,
        'kilometer': 1000.0,
        'cm': 0.01,
        'centimeter': 0.01,
        'mm': 0.001,
        'millimeter': 0.001,
        'in': 0.0254,
        'inches' : 0.0254,
        'ft': 0.3048,
        'feet': 0.3048,
        'yd': 0.9144,
        'yard': 0.9144,
        'mi': 1609.34,
        'mile': 1609.34,
    }
    
    # Check if the units are valid
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid units provided.")
    
    # Convert the value to meters
    value_in_meters = value * conversion_factors[from_unit]
    
    # Convert the value from meters to the target unit
    converted_value = value_in_meters / conversion_factors[to_unit]
    
    # Round to avoid floating point precision issues
    return round(converted_value, 10)