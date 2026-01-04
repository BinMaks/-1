m = int(input("Количество элементов: "))
seq = [int(input(f"Элемент {i+1} (0 или 1): ")) for i in range(m)]
min_length = float('inf')
current_length = 0
for num in seq:
    if num == 0:
        current_length += 1
    else:
        if current_length > 0:
            min_length = min(min_length, current_length)
        current_length = 0
if current_length > 0:
    min_length = min(min_length, current_length)

if min_length == float('inf'):
    print("Нулевых отрезков нет")
else:
    print(f"Наименьшая длина отрезка из нулей: {min_length}")