
a, b = 1, 1
total_sum = 0
while a <= 1000:
    total_sum += a
    a, b = b, a + b
print(f"Сумма чисел Фибоначчи, не превосходящих 1000: {total_sum}")


n = int(input("Введите n (n > 1): "))
a, b = 1, 1
while a <= n:
    a, b = b, a + b
print(f"Первое число Фибоначчи, большее {n}: {a}")