m = int(input("m: "))
x = [int(input()) for _ in range(m)]
last_idx = -1
for i in range(m):
    if x[i] % 100 == 12:
        last_idx = i
if last_idx != -1:
    print("Последний элемент, оканчивающийся на 12, на позиции:", last_idx + 1)
else:
    print("Элементов, оканчивающихся на 12, нет.")