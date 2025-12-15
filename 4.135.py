month_num = int(input("Введите номер месяца (1–12): "))
if 1 <= month_num <= 12:
    if month_num in [12, 1, 2]:
        print("Зима")
    elif month_num in [3, 4, 5]:
        print("Весна")
    elif month_num in [6, 7, 8]:
        print("Лето")
    else:
        print("Осень")
else:
    print("Некорректный номер месяца")