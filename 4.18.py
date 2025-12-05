import math
radius = float(input("Радиус круга: "))
side = float(input("Сторона квадрата: "))
diameter = 2 * radius
diagonal = side * math.sqrt(2)
if diameter <= side:
    print("Круг уместится в квадрате. ")
else:
    print("Круг не уместится в квадрате. ")
if diagonal <= diameter:
    print("Квадрат уместится в круге. ")
else:
    print("Квадрат не уместится в круге. ")