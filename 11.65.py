arr = [int(x) for x in input("Введите элементы массива: ").split()]

sum_greater_20 = sum(x for x in arr if x > 20)
if sum_greater_20 > 100:
    print("Сумма элементов > 20 превышает 100")
else:
    print("Сумма элементов > 20 не превышает 100")

sum_less_50 = sum(x for x in arr if x < 50)
if sum_less_50 % 2 == 0:
    print("Сумма элементов < 50 — чётное число")
else:
    print("Сумма элементов < 50 — нечётное число")