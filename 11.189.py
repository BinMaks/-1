arr = list(map(int, input("Элементы массива: ").split()))
first = arr.index(5)
last = len(arr) - 1 - arr[::-1].index(5)
print(f"Первый: {first}, последний: {last}")