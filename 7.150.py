n = int(input("Количество чисел: "))
seq = [int(input(f"Число {i+1}: ")) for i in range(n)]

max_length = 0
current_length = 0

for num in seq:
    if num % 2 == 0:
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 0

print(f"Наибольшая длина отрезка из четных чисел: {max_length}")