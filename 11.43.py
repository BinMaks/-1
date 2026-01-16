arr = [int(x) for x in input("Введите элементы массива: ").split()]
result = sum(arr[i] * (-1)**i for i in range(len(arr)))
print(f"Знакопеременная сумма: {result}")