import math
x1, y1 = map(float,input("Введите координаты вершины A(x1 y1):").split())
x2, y2 = map(float,input("Введите координаты вершины B(x2 y2):").split())
x3, y3 = map(float,input("Введите координаты вершины C(x3 y3):").split())
ab=math.sqrt((x2-x1)**2+(y2-y1)**2)
bc=math.sqrt((x3-x2)**2+(y3-y2)**2)
ca=math.sqrt((x1-x3)**2+(y1-y3)**2)
perimeter=ab+bc+ca
area=0.5*abs((x1-x3)*(y2-y3)-(y1-y3)*(x2-x3))
print(f"Периметр треугольника: {perimeter:.3f} ед.")
print(f"Площадь треуггольника: {area:.3f} кв.ед.")