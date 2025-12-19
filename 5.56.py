import math

n = 1000
dx = math.pi / n
area = 0
for i in range(n):
    x = i * dx
    area += math.sin(x) * dx
print(f"Приближённая площадь: {area:.4f}")