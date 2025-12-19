
n = int(input("Введите n: "))
sum_fractions = sum(1/i for i in range(2, n + 1))
print(f"Сумма дробей: {sum_fractions:.4f}")