import math
a, b = map(float, input("введите два числа: ").split())
sqrt_b = math.sqrt(b)
if sqrt_b < a:
    b *= 5
print(f"Результат: {a}, {b}")