arr = [float(x) for x in input("Введите элементы массива: ").split()]
m = float(input("Введите число m: "))
filtered = [x for x in arr if x < m]
if filtered:
    avg = sum(filtered) / len(filtered)
    print(f"Среднее арифметическое элементов < {m}: {avg}")
else:
    print("Нет элементов меньше m")