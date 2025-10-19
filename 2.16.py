import math
a=float(input("Введите длину первого катета"))
b=float(input("Введите длину второго катета"))
c=math.sqrt(a**2+b**2)
perimeter=a+b+c
print(f"Периметр треугольника:{perimeter:.2f}")