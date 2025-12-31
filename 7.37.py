
import math
a = float(input("Введите сторону основания: "))
h = float(input("Введите высоту: "))
S_base = (math.sqrt(3) / 4) * a**2
V = S_base * h
print("Объем призмы:", V)