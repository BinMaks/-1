month_num = int(input("Введите номер месяца (1–12): "))
is_leap = input("Год високосный? (да/нет): ").lower() == "да"
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 1 <= month_num <= 12:
    if month_num == 2 and is_leap:
        print("В феврале 29 дней")
    else:
        print(f"В месяце {days_in_month[month_num - 1]} дней")
else:
    print("Некорректный номер месяца")