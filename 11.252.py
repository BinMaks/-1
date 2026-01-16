a = list(map(int, input("Массив из 20 элементов: ").split()))
arr1 = [a[i] for i in range(0, 20, 2)]
arr2 = [a[i] for i in range(1, 20, 2)]
print("Четные индексы:", arr1)
print("Нечетные индексы:", arr2)