import random

N = 100000
count = 0
for _ in range(N):
    x = random.uniform(0, 3)
    y = random.uniform(0, 9)
    if y >= x**2:
        continue
    count += 1
area = (count / N) * 27
print(f"Площадь фигуры: {area}")