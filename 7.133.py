sequence = []
while True:
    num = float(input("Введите число (1000 для завершения): "))
    if num == 1000:
        break
    sequence.append(num)

max_count = 1
current_count = 1
for i in range(1, len(sequence)):
    if sequence[i] == sequence[i-1]:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 1
print(f"Максимальное количество подряд идущих равных чисел: {max_count}")