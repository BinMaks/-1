arr = list(map(int, input("Элементы массива: ").split()))
n = int(input("Значение n: "))
found = False
for i, elem in enumerate(arr):
    if elem == n:
        found = True
        break
if found:
    print(f"Элементы до {n}: {arr[:i]}")
else:
    print("Элементов, равных n, нет — печатаем все элементы:", arr)