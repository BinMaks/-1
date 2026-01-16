arr = [int(x) for x in input("Введите элементы массива: ").split()]
a = int(input("Введите число a: "))

sum_not_exceed_20 = sum(x for x in arr if x <= 20)
print(f"Сумма элементов ≤ 20: {sum_not_exceed_20}")

sum_greater_a = sum(x for x in arr if x > a)
print(f"Сумма элементов > {a}: {sum_greater_a}")