arr = list(map(int, input("Введите элементы массива: ").split()))
max_idx = arr.index(max(arr))
min_idx = arr.index(min(arr))
if max_idx < min_idx:
    max_idx, min_idx = min_idx, max_idx
del arr[max_idx]
del arr[min_idx]
arr.append(0)
arr.append(0)
print(arr)