arr = list(map(int, input("Введите элементы массива: ").split()))
first_negative_idx = None
last_positive_idx = None
for i, x in enumerate(arr):
    if x < 0 and first_negative_idx is None:
        first_negative_idx = i
    if x > 0:
        last_positive_idx = i

if first_negative_idx is not None and last_positive_idx is not None:
    arr[first_negative_idx], arr[last_positive_idx] = arr[last_positive_idx], arr[first_negative_idx]
print(arr)