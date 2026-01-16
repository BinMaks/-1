temperatures = [float(x) for x in input("Введите температуры за 30 дней: ").split()]
sum_positive = sum(t for t in temperatures if t > 0)
sum_negative = sum(t for t in temperatures if t < 0)
count_positive = sum(1 for t in temperatures if t > 0)
print(f"Сумма положительных температур: {sum_positive}")
print(f"Сумма отрицательных температур: {sum_negative}")
print(f"Дней с положительной температурой: {count_positive}")