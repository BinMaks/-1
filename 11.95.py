arr = [float(x) for x in input("Введите элементы массива: ").split()]
total_sum = sum(arr)
result = [(i, x) for i, x in enumerate(arr) if x > total_sum]

if result:
    print("Элементы > суммы всех элементов и их номера:")
    for idx, val in result:
        print(f"Индекс {idx}: {val}")
else:
    print("Нет таких элементов")