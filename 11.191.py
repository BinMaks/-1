arr = list(map(int, input("Элементы массива: ").split()))
first_zero = arr.index(0)
print(arr[:first_zero] + arr[first_zero + 1:])


arr = list(map(int, input("Элементы массива: ").split()))
last_zero = len(arr) - 1 - arr[::-1].index(0)
print(arr[:last_zero] + arr[last_zero + 1:])