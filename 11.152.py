
arr = list(map(int, input("Введите элементы массива: ").split()))
n = len(arr)
arr[:n//2], arr[n//2:] = arr[n//2:], arr[:n//2]
print(arr)


arr = list(map(int, input("Введите элементы массива: ").split()))
for i in range(0, len(arr) - 1, 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)


arr = list(map(int, input("Введите элементы массива: ").split()))
arr.reverse()
print(arr)