def area_triangle(a,b,c):
    s = (a + b + c) / 2                             # semi-perimeter calculation with equation
    a = (s * (s - a) * (s - b) * (s - c)) ** (1/2)  # area of triangle calculation with Heron's formula
    return a