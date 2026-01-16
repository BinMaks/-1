arr = list(map(int, input("Введите 30 элементов неубывающего массива: ").split()))
distinct_count = len(set(arr))
print(f"Количество различных чисел: {distinct_count}")