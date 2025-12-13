a, b, c = map(float, input("Введите стороны треугольника (a b c): ").split())
if (a+b > c ) and (a + c > b) and (b + c > a):
    print("Треугольник существует")
else:
    print("Треугольник не существует ")
