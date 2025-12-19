x = 2
n = int(input("Введите n: "))
sum_series = x
power_x = x
for i in range(2, n + 1):
    power_x *= x  
    sum_series += power_x / i
print(f"Сумма: {sum_series:.4f}")