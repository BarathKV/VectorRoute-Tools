def percentage_calc(part:int, whole:int) -> float:
    """
    percentage_calc function.

    Args:
        part (int): Input parameter.
        whole (int): Input parameter.

    Returns:
        float: Function result.
    """
    if whole == 0:
        return 0
    return (part / whole) * 100