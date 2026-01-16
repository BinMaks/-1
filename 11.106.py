arr = list(map(int, input("Введите элементы массива: ").split()))
counts = {}
for x in arr:
    counts[x] = counts.get(x, 0) + 1
if any(count == 2 for count in counts.values()) and all(count <= 2 for count in counts.values()):
    print("В массиве ровно два одинаковых элемента")
else:
    print("Условие не выполнено")