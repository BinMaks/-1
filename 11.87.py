arr = [float(x) for x in input("Введите элементы массива: ").split()]
elements_above_10 = [x for x in arr if x > 10]
if elements_above_10:
    avg = sum(elements_above_10) / len(elements_above_10)
    print(f"Среднее арифметическое элементов > 10: {avg}")
else:
    print("Нет элементов больше 10")