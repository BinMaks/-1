arr = [int(x) for x in input("Введите элементы массива: ").split()]
positives = sum(1 for x in arr if x > 0)
negatives = sum(1 for x in arr if x < 0)
print(f"Положительных элементов: {positives}, отрицательных: {negatives}")