import math

def f(x):
    return 0.4 * (x + 2) ** 2 + 1
x1 = 0
x2 = -2 + math.sqrt((2 - 1) / 0.4)
n = 1000
dx = (x2 - x1) / n
area = 0
for i in range(n):
    x = x1 + i * dx
    y = f(x)
    if y < 2:
        area += y * dx
print(f"Площадь: {area:.4f}")