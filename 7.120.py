
n = int(input("n: "))
c = [int(input()) for _ in range(n)]

last_idx = -1
for i in range(n):
    if c[i] == 25:
        last_idx = i
if last_idx != -1:
    print("Последний элемент 25 на позиции:", last_idx + 1)
else:
    print("Элементов 25 нет.")