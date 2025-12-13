a = int(input("Введите a (вертикаль фигуры): "))
b = int(input("Введите b (горизонталь фигуры): "))
c = int(input("Введите c (вертикаль цели): "))
d = int(input("Введите d (горизонталь цели): "))
figure = input("Введите фигуру (ладья, слон, король, ферзь, белая пешка, чёрная пешка, конь): ")
if figure == "ладья":
    if a == c or b == d:
        print("Угрожает!")
    else:
        print("Не угрожает.")
elif figure == "слон":
    if abs(a - c) == abs(b - d):
        print("Угрожает!")
    else:
        print("Не угрожает.")
elif figure == "король":
    if abs(a - c) <= 1 and abs(b - d) <= 1:
        print("Угрожает!")
    else:
        print("Не угрожает.")
elif figure == "ферзь":
    if a == c or b == d or abs(a - c) == abs(b - d):
        print("Угрожает!")
    else:
        print("Не угрожает.")
elif figure == "белая пешка":
    if a == c and b + 1 == d:
        print("Угрожает (обычный ход)!")
    elif abs(a - c) == 1 and b + 1 == d:
        print("Угрожает (взятие)!")
    else:
        print("Не угрожает.")
elif figure == "чёрная пешка":
    if a == c and b - 1 == d:
        print("Угрожает (обычный ход)!")
    elif abs(a - c) == 1 and b - 1 == d:
        print("Угрожает (взятие)!")
    else:
        print("Не угрожает.")
elif figure == "конь":
    if (abs(a - c) == 2 and abs(b - d) == 1) or (abs(a - c) == 1 and abs(b - d) == 2):
        print("Угрожает!")
    else:
        print("Не угрожает.")
else:
    print("Неизвестная фигура.")