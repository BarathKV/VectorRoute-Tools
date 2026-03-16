def part_to_percent_calc(percentage: float, whole: float) -> float:
    """
    Calculate the numerical value of a given percentage of a whole.

    Args:
        percentage (float): The percentage value (e.g., 20 for 20%).
        whole (float): The total value to calculate from.

    Returns:
        float: The resulting part of the whole.
    """
    # If the total is 0, any percentage of it remains 0
    if whole == 0:
        return 0.0
        
    return (percentage / 100) * whole