k = int(input("k: "))
b = [int(input()) for _ in range(k)]

last_idx = -1
for i in range(k):
    if b[i] < 0:
        last_idx = i
print("Последний отрицательный элемент на позиции:", last_idx + 1)