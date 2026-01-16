arr = list(map(int, input("Элементы массива: ").split()))
first_odd_idx = -1
for i, elem in enumerate(arr):
    if elem % 2 == 1:
        first_odd_idx = i
        break
if first_odd_idx != -1:
    print(f"Номер первого нечетного элемента: {first_odd_idx}")
else:
    print("Нечетных элементов нет.")

arr = list(map(int, input("Элементы массива: ").split()))
first_13_idx = -1
for i, elem in enumerate(arr):
    if elem % 13 == 0:
        first_13_idx = i
        break
if first_13_idx != -1:
    print(f"Номер первого элемента, кратного 13: {first_13_idx}")
else:
    print("Элементов, кратных 13, нет.")