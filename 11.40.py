import math
arr = [int(x) for x in input("Введите элементы массива: ").split()]
index = int(input("Введите индекс элемента для извлечения корня: "))
if 0 <= index < len(arr) and arr[index] >= 0:
    print(f"Квадратный корень из элемента {arr[index]}: {math.sqrt(arr[index])}")
else:
    print("Неверный индекс или отрицательное число!")

arr = [int(x) for x in input("Введите элементы массива: ").split()]
i = int(input("Индекс первого элемента: "))
j = int(input("Индекс второго элемента: "))
if 0 <= i < len(arr) and 0 <= j < len(arr):
    avg = (arr[i] + arr[j]) / 2
    print(f"Среднее арифметическое: {avg}")
else:
    print("Неверный индекс!")