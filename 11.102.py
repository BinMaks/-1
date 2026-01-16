
arr = [float(x) for x in input("Введите элементы массива: ").split()]
avg = sum(arr) / len(arr)
closest = min(arr, key=lambda x: abs(x - avg))
print(f"Элемент, ближайший к среднему ({avg}): {closest}")