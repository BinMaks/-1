
arr = list(map(float, input("Введите элементы массива: ").split()))
m, n = map(int, input("Введите m и n для обмена: ").split())
arr[1], arr[4] = arr[4], arr[1]
print(f"а) После обмена 2-го и 5-го: {arr}")
arr[m-1], arr[n-1] = arr[n-1], arr[m-1]
print(f"б) После обмена {m}-го и {n}-го: {arr}")
max_val = max(arr)
max_idx = arr.index(max_val)
arr[2], arr[max_idx] = arr[max_idx], arr[2]
print(f"в) После обмена 3-го и максимального: {arr}")