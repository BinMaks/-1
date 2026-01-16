arr = list(map(int, input("Введите элементы массива: ").split()))
del arr[2]
arr.append(0)
print(arr)

arr = list(map(int, input("Введите элементы массива: ").split()))
k = int(input("Введите k: ")) - 1
del arr[k]
arr.append(0)
print(arr)