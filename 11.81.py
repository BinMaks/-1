
arr = [int(x) for x in input("Введите элементы массива: ").split()]
even_pairs = sum(1 for i in range(len(arr) - 1) if arr[i] % 2 == 0 and arr[i+1] % 2 == 0)
print(f"Пар соседних чётных чисел: {even_pairs}")