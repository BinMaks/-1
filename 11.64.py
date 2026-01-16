arr = [float(x) for x in input("Введите элементы массива: ").split()]
sum_positive = sum(x for x in arr if x > 0)
sum_negative = sum(x for x in arr if x < 0)

if sum_negative != 0:
    result = sum_positive / abs(sum_negative)
    print(f"Частное: {result}")
else:
    print("Нет отрицательных элементов")