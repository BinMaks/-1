g = int(input("Введите год: "))
m = int(input("Введите номер месяца (1–12): "))
n = int(input("Введите число месяца: "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if n == 1:
    if m == 1:
        prev_g, prev_m, prev_n = g - 1, 12, 31
    else:
        prev_m = m - 1
        prev_n = days_in_month[prev_m - 1]
        prev_g = g
else:
    prev_g, prev_m, prev_n = g, m, n - 1
print(f"Предыдущий день: {prev_g}.{prev_m}.{prev_n}")
if n == days_in_month[m - 1]:
    if m == 12:
        next_g, next_m, next_n = g + 1, 1, 1
    else:
        next_m = m + 1
        next_n = 1
        next_g = g
else:
    next_g, next_m, next_n = g, m, n + 1
print(f"Следующий день: {next_g}.{next_m}.{next_n}")