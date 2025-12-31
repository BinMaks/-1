import math
a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))
ma = 0.5 * math.sqrt(2 * b**2 + 2 * c**2 - a**2)
print("Длина медианы:", ma)