def clamp(num:float, min_value:float, max_value:float) -> float:
    num = max(min(num, max_value), min_value)
    return num

def scale(x:float, in_min:float, in_max:float, out_min:float, out_max:float):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min