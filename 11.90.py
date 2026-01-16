
arr = [float(x) for x in input("Введите элементы массива: ").split()]
positives = [x for x in arr if x > 0]
negatives = [x for x in arr if x < 0]

if positives:
    avg_pos = sum(positives) / len(positives)
    print(f"Среднее положительных элементов: {avg_pos}")
else:
    print("Нет положительных элементов")

if negatives:
    avg_neg = sum(negatives) / len(negatives)
    print(f"Среднее отрицательных элементов: {avg_neg}")
else:
    print("Нет отрицательных элементов")