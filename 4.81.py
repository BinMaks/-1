a, b, c = map(float, input("Введите стороны треугольника (a b c): ").split())
if not ((a + b > c) and (a + c > b) and (b + c > a)):
    print("Треугольник не существует.")
else:
    sides = sorted([a, b, c])
    a, b, c = sides[0], sides[1], sides[2]
    if a**2 + b**2 > c**2:
        angle_type = "остроугольный"
    elif a**2 + b**2 < c**2:
        angle_type = "тупоугольный"
    else:
        angle_type = "прямоугольный"
    print(f"По углам треугольник {angle_type}.")
    if a == b == c:
        feature = "равносторонний"
    elif a == b or b == c or a == c:
        feature = "равнобедренный"
    else:
        feature = "разносторонний"
    print(f"По сторонам треугольник {feature}.")