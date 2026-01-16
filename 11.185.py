arr = list(map(int, input("28 элементов: ").split()))
k = int(input("k: "))
arr = arr[k:] + arr[:k]
print(arr)