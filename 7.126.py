a = [float(input()) for _ in range(15)]

first_neg_idx = -1
for i in range(15):
    if a[i] < 0:
        first_neg_idx = i
        break

if first_neg_idx != -1:
    print("Есть отрицательные числа. Первое на позиции:", first_neg_idx + 1)
else:
    print("Отрицательных чисел нет.")