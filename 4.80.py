a, b, c = map(float, input("Введите стороны треугольника (a b c): ").split())
sides = sorted([a, b, c])
a, b, c = sides[0], sides[1], sides[2]
if a ** 2 + b ** 2 == c ** 2:
    print("Треугольник прямоугольный")
else:
    print("Треугольник не прямоугольный")