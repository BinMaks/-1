a = float(input("длина отрезка a: "))
b = float(input("Длина отрезка b: "))
c = float(input("Длина отрезка с: "))
if a + b > c and a + c > b and b + c > a:
    print("Треугольник можно построить")
else:
    print("Треугольник нельзя построить")