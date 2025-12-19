
n = int(input("Введите n: "))
sum_series = 0
power_of_3 = 1  # 3^0 = 1
for i in range(n + 1):
    sum_series += 1 / power_of_3
    power_of_3 *= 3  # Увеличиваем степень 3
print(f"Сумма: {sum_series:.4f}")