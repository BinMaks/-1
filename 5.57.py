import math

def f(x):
    return 0.3 * (x - 1) ** 2 + 3
x1 = 1 - math.sqrt((2 - 3) / 0.3)
x2 = 1 + math.sqrt((4 - 3) / 0.3)
n = 1000
dx = (x2 - x1) / n
area = 0
for i in range(n):
    x = x1 + i * dx
    y = f(x)
    if y > 2 and y < 4:
        area += (y - 2) * dx  
print(f"Площадь: {area:.4f}")