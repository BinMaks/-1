import math
R=float(input("Введите внешний радиус:"))
r=float(input("Введите внутренний радиус:"))
if R<=r:
    print("Внешний радиус должен быть больше внутреннего")
else:
    area=math.pi*(R**2-r**2)
    print(f"Площадь кольца: {area:.2f}")