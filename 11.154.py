arr = list(map(int, input("Введите 15 элементов массива: ").split()))
arr[2:10] = arr[2:10][::-1]
print(arr)


arr = list(map(int, input("Введите 15 элементов массива: ").split()))
k, s = map(int, input("Введите k и s: ").split())
arr[k:s] = arr[k:s][::-1]
print(arr)