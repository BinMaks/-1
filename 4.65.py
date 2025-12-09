import math
x = float(input("x: "))
y = float(input("y: "))
R = float(input("Радиус R: "))
distance = math.sqrt(x ** 2 + y ** 2)
if distance <= R:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")