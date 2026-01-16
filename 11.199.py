
arr = list(map(float, input("Вещественные числа: ").split()))
first_neg_idx = -1
for i, elem in enumerate(arr):
    if elem < 0:
        first_neg_idx = i
        break
if first_neg_idx != -1:
    print(f"Элементы после первого отрицательного: {arr[first_neg_idx+1:]}")
else:
    print("Отрицательных элементов нет.")

arr = list(map(float, input("Вещественные числа: ").split()))
last_neg_idx = -1
for i, elem in enumerate(arr):
    if elem < 0:
        last_neg_idx = i
if last_neg_idx != -1:
    print(f"Элементы слева от последнего отрицательного: {arr[:last_neg_idx]}")
else:
    print("Отрицательных элементов нет.")