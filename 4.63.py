a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))
sides = sorted([a, b, c])
a, b, с = sides[0], sides[1], sides[2]
if c ** 2 < a ** 2 + b ** 2:
    print("Остроугольный треугольник")
elif c ** 2 == a ** 2 + b ** 2:
    print("прямоугольный треугольник")
else:
    print("Тупоугольный треугольник ")