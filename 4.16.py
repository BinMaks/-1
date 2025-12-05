import math
a = float(input("Коэффициент a: "))
b = float(input("Коэффицицент b: "))
c = float(input("Коэффициент с: "))
discriminant = b ** 2 - 4 * a * c
if discriminant >= 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Корни уравнения: x1 = {x1}, x2 = {x2}")
else:
    print("Уравнение не имеет действительных корней. ")