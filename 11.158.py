arr = list(map(int, input("Введите элементы массива: ").split()))
max_idx = arr.index(max(arr))
del arr[max_idx]
arr.append(0)
print(arr)

arr = list(map(int, input("Введите элементы массива: ").split()))
min_idx = arr.index(min(arr))
del arr[min_idx]
arr.append(0)
print(arr)