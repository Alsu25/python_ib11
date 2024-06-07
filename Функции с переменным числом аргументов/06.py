def solve(*coefficients):

    if len(coefficients) == 0 or len(coefficients) > 3:
        return None
    a, b, c = coefficients

    if len(coefficients) == 3:
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return None
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return [x1, x2]

    elif len(coefficients) == 2:
        x = -c / b
        return [x]

    else:
        if c == 0:
            return None
        else:
            return None
