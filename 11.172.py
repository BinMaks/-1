arr = list(map(int, input("Введите элементы массива: ").split()))
n = int(input("Значение n: "))
m = int(input("Значение m: "))
for i, x in enumerate(arr):
    if x > n:
        arr.insert(i, n)
        break
else:
    arr.append(n)
for i in range(len(arr) - 1, -1, -1):
    if arr[i] < m:
        arr.insert(i + 1, m)
        break
else:
    arr.insert(0, m)
print(arr)