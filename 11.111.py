arr = list(map(int, input("Введите элементы массива: ").split()))
max_length = 0
current_length = 0
for x in arr:
    if x % 2 == 1:  # нечётное
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 0
print(f"Максимальная длина отрезка из нечетных чисел: {max_length}")