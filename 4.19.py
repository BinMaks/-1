import math
radius = float(input("Радиус круга: "))
side = float(input("Сторона  треугольника: "))
diameter = 2 * radius
diagonal = side * math.sqrt(3) / 2
if diameter <= side:
    print("Круг уместится в треугольники. ")
else:
    print("Круг не уместится в треугольники. ")
if diagonal <= diameter:
    print("Треугольник уместится в круге. ")
else:
    print("Треугольник не уместится в круге. ")