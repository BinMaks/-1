arr = list(map(int, input("Убывающий массив: ").split()))
a = int(input("Число a: "))
for i, x in enumerate(arr):
    if x < a:
        print(f"Номер первого элемента < {a}: {i + 1}")
        break
else:
    print("Нет элементов меньше a")