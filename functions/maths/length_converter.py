def length_converter(value: float, from_unit: str, to_unit: str) -> float:
    """
    length_converter function.

    Args:
        value (float): Input parameter.
        from_unit (str): Input parameter.
        to_unit (str): Input parameter.

    Returns:
        float: Function result.
    """

    # Define conversion factors relative to 1 meter
    factors = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344
    }

    # Map all possible aliases to the keys in 'factors'
    unit_map = {
        # Metric
        'm': 'm', 'meter': 'm', 'meters': 'm',
        'km': 'km', 'kilometer': 'km', 'kilometers': 'km',
        'cm': 'cm', 'centimeter': 'cm', 'centimeters': 'cm',
        'mm': 'mm', 'millimeter': 'mm', 'millimeters': 'mm',
        # Imperial
        'in': 'in', 'inch': 'in', 'inches': 'in',
        'ft': 'ft', 'foot': 'ft', 'feet': 'ft',
        'yd': 'yd', 'yard': 'yd', 'yards': 'yd',
        'mi': 'mi', 'mile': 'mi', 'miles': 'mi'
    }

    # Normalize inputs
    from_key = unit_map.get(from_unit.lower().strip())
    to_key = unit_map.get(to_unit.lower().strip())

    if not from_key or not to_key:
        raise ValueError(f"Invalid units: '{from_unit}' or '{to_unit}' not supported.")

    # Convert to meters, then to target unit
    value_in_meters = value * factors[from_key]
    return value_in_meters / factors[to_key]