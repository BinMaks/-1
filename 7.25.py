import math
a = float(input("Введите сторону основания: "))
l = float(input("Введите апофему: "))
S_base = a**2
S_side = 2 * a * l
print("Площадь поверхности:", S_base + S_side)