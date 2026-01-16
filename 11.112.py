arr = list(map(int, input("Введите элементы массива: ").split()))
max_val = max(arr)
min_val = min(arr)
max_idx = arr.index(max_val)
min_idx = arr.index(min_val)
diff = max_val - min_val
print(f"Максимальный элемент: {max_val} (индекс {max_idx})")
print(f"Минимальный элемент: {min_val} (индекс {min_idx})")
print(f"Разница: {diff}")