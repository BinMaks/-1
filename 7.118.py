
n = int(input("n: "))
a = [int(input()) for _ in range(n)]


last_idx = -1
for i in range(n):
    if a[i] == 10:
        last_idx = i
print("Последний элемент 10 на позиции:", last_idx + 1)


first_idx = -1
for i in range(n):
    if a[i] == 10:
        first_idx = i
        break
print("Первый элемент 10 на позиции:", first_idx + 1)