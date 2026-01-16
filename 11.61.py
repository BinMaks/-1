arr = [int(x) for x in input("Введите элементы массива: ").split()]
sum_even_indices = sum(arr[i] for i in range(1, len(arr), 2))
print(f"Сумма элементов с четными номерами: {sum_even_indices}")