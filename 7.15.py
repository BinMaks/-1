import math
R = float(input("Введите внешний радиус: "))
r = float(input("Введите внутренний радиус: "))
print("Площадь:", math.pi * (R**2 - r**2))