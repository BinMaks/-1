arr = [int(x) for x in input("Введите элементы массива: ").split()]
indices = [i for i, x in enumerate(arr) if x % 10 == 0]
print("Индексы элементов, оканчивающихся на 0:", indices)