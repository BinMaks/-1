import math

n = int(input("Количество снарядов: "))
g = 9.8
hits = 0
for _ in range(n):
    alpha, v0, t, R, H = map(float, input("α, V0, t, R, H: ").split())
    x = v0 * t * math.cos(math.radians(alpha))
    y = v0 * t * math.sin(math.radians(alpha)) - (g * t**2) / 2
    if abs(x - R) < 0.1 and abs(y - H) < 0.1:
        hits += 1
percentage = (hits / n) * 100
print("Процент попаданий:", percentage)