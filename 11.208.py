
arr = list(map(int, input("Массив: ").split()))
last_pair_idx = -1
for i in range(len(arr) - 1):
    if arr[i] % 2 == 0 and arr[i+1] % 2 == 0:
        last_pair_idx = i
if last_pair_idx != -1:
    print("Элементы до последней пары четных:", arr[:last_pair_idx])
else:
    print("Нет пары соседних четных элементов")