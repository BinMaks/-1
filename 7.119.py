n = int(input("n: "))
b = [int(input()) for _ in range(n)]

last_idx = -1
for i in range(n):
    if b[i] > 100:
        last_idx = i
print("Последний элемент > 100 на позиции:", last_idx + 1)