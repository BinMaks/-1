sequence = [int(input(f"Число {i+1}: ")) for i in range(20)]
max_count = 1
current_count = 1
for i in range(1, 20):
    if sequence[i] == sequence[i-1]:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 1
print(f"Максимальное количество подряд идущих равных чисел: {max_count}")