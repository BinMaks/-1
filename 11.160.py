arr = list(map(int, input("Введите элементы массива: ").split()))
for i, x in enumerate(arr):
    if x < 0:
        del arr[i]
        arr.append(0)
        break
print(arr)

arr = list(map(int, input("Введите элементы массива: ").split()))
even_idx = None
for i, x in enumerate(arr):
    if x % 2 == 0:
        even_idx = i
if even_idx is not None:
    del arr[even_idx]
    arr.append(0)
print(arr)