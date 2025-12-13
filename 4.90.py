m, n = map(int, input("Введите месяц (m) и число (n): ").split())
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if n == 1:
    prev_m = m - 1
    if prev_m == 0:
        prev_m = 12
    prev_n = days_in_month[prev_m - 1]
else:
    prev_m = m
    prev_n = n - 1
print(f"Предыдущий день: {prev_m} месяц, {prev_n} число")
if n == days_in_month[m - 1]:
    next_m = m + 1
    if next_m == 13:
        next_m = 1
    next_n = 1
else:
    next_m = m
    next_n = n + 1
print(f"Следующий день: {next_m} месяц, {next_n} число")