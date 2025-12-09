import math

a = float(input("Коэффициент a: "))
b = float(input("Коэффициент b: "))
c = float(input("Коэффициент c: "))
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Два корня: x1 = {x1:.2f}, x2 = {x2:.2f}")
elif discriminant == 0:
    x = -b / (2 * a)
    print(f"Один корень: x = {x:.2f}")
else:
    print("Нет действительных корней")