n = int(input("Введите n: "))
sum_series = sum(i**2 for i in range(n, 2 * n + 1))
print(f"Сумма: {sum_series}")