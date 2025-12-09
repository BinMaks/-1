import math
a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))
p = (a + b + c) / 2
if a + b > c and a + c > b and b + c > a:
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Площадь треугольника: {area:.2f}")
else:
    print("Треугольник не существует")