m = int(input("Введите номер месяца (1–12): "))
n = int(input("Введите число месяца: "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if n == 1:
    if m == 1:
        prev_m, prev_n = 12, 31
    else:
        prev_m, prev_n = m - 1, days_in_month[m - 2]
else:
    prev_m, prev_n = m, n - 1
print(f"Предыдущий день: {prev_m}.{prev_n}")
if n == days_in_month[m - 1]:
    if m == 12:
        next_m, next_n = 1, 1
    else:
        next_m, next_n = m + 1, 1
else:
    next_m, next_n = m, n + 1
print(f"Следующий день: {next_m}.{next_n}")