
arr = list(map(int, input("Введите элементы массива: ").split()))
seen = set()
for x in arr:
    if x in seen:
        print(f"Найдены одинаковые элементы: {x}")
        break
    seen.add(x)