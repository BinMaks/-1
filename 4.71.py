import math
g = 9.8
v0 = float(input("Начальная скорость (v0): "))
alpha = float(input("Угол выстрела (в радианах): "))
R = float(input("Расстояние до цели (R): "))
P = float(input("Высота цели (P): "))
t = R / (v0 * math.cos(alpha))
y = v0 * t * math.sin(alpha) - 0.5 * g * t**2
if y >= P:
    print("Снаряд поразит цель!")
else:
    print(f"Снаряд не поразит цель. Максимальная высота: {y:.2f} м, высота цели {P} м.")