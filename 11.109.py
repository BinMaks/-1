arr = list(map(int, input("Введите 20 элементов неубывающего массива: ").split()))
max_equal_count = 1
current_equal_count = 1
distinct_count = 1
for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        current_equal_count += 1
        max_equal_count = max(max_equal_count, current_equal_count)
    else:
        current_equal_count = 1
        distinct_count += 1
print(f"Максимальное количество подряд идущих равных элементов: {max_equal_count}")
print(f"Количество различных чисел: {distinct_count}")