n = int(input("Введите количество месяцев n:"))
start_month = 1
start_year = 1990
final_month_number = start_month + n
if final_month_number % 12 == 0:
    x = 12
else:
    x = final_month_number % 12
print(f"Месяц: {x}")