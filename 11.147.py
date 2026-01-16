
arr = list(map(float, input("Введите элементы массива: ").split()))
max_mod = max(arr, key=abs)
arr[arr.index(max_mod)] = -max_mod
print(f"Массив после изменения: {arr}")