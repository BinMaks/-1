arr = list(map(float, input("Введите элементы массива: ").split()))
min_val = min(arr)
max_val = max(arr)
min_indices = [i for i, x in enumerate(arr) if x == min_val]
max_indices = [i for i, x in enumerate(arr) if x == max_val]
print(f"Индексы элементов с минимальным значением ({min_val}): {min_indices}")
print(f"Индексы элементов с максимальным значением ({max_val}): {max_indices}")