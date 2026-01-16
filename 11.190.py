
arr = list(map(int, input("Элементы массива: ").split()))
first = -1
last = -1
for i, x in enumerate(arr):
    if x > 65530:
        if first == -1:
            first = i
        last = i
print(f"Первый: {first}, последний: {last}")