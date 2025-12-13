k = int(input("введите номер дня года (1-365): "))
if 1 <= k <= 365:
    day_of_week = k % 7
    if day_of_week == 0 or day_of_week == 6:
        print(f"{k}-й день года - выходной. ")
    else:
        print(f"{k}-й день года - рабочий.")
else:
    print("Ошибка: число должно быть от 1 до 365.")