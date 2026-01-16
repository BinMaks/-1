arr = [float(x) for x in input("Введите элементы массива: ").split()]
min_val, max_val = min(arr), max(arr)
avg_min_max = (min_val + max_val) / 2
result = [(i, x) for i, x in enumerate(arr) if x > avg_min_max]
if result:
    print("Элементы > среднего min и max и их номера:")
    for idx, val in result:
        print(f"Индекс {idx}: {val}")
else:
    print("Нет таких элементов")