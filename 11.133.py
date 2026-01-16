
arr = list(map(float, input("Введите элементы массива: ").split()))
min_val = min(arr)
max_val = max(arr)
min_index = arr.index(min_val)
max_index = arr.index(max_val)
if min_index < max_index:
    print("Минимальное значение встречается раньше")
elif min_index > max_index:
    print("Максимальное значение встречается раньше")
else:
    print("Минимальное и максимальное значения встречаются одновременно (на одной позиции)")