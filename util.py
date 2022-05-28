def clamp(num:float, min_value:float, max_value:float) -> float:
    num = max(min(num, max_value), min_value)
    return num