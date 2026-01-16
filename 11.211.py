arr = list(map(int, input("Массив: ").split()))
last_triplet_idx = -1
for i in range(1, len(arr) - 1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        last_triplet_idx = i
if last_triplet_idx != -1:
    print("Элементы до последней тройки:", arr[:last_triplet_idx])
else:
    print("Нет такой тройки")