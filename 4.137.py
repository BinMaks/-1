month_num = int(input("Введите номер месяца (1–12): "))
if month_num in [1, 3, 5, 7, 8, 10, 12]:
    print("31 день")
elif month_num in [4, 6, 9, 11]:
    print("30 дней")
elif month_num == 2:
    print("28 дней")
else:
    print("Некорректный номер месяца")