def remainder(a, b):
    """Возвращает остаток от деления a на b"""
    if b == 0:
        raise ValueError("На ноль делить нельзя")
    return a % b
