import math
x1, y1 = map(float,input("Введите координаты  A(x1 y1):").split())
x2, y2 = map(float,input("Введите координаты  B(x2 y2):").split())
x3, y3 = map(float,input("Введите координаты  C(x3 y3):").split())
x4, y4 = map(float,input("Введите координаты  D(x4 y4):").split())
def triangle_area(x1,y1,x2,y2,x3,y3):
    return 0.5* abs((x1-x3)*(y2-y3)-(y1-y3)*(x2-x3))
area_abc = triangle_area(x1,y1,x2,y2,x3,y3)
area_acd= triangle_area(x1, y1, x3, y3, x4, y4)
total_area = area_abc+area_acd
print(f"Площадь четырёхуггольника: {total_area:.4f} кв. ед.")