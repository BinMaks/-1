seq = list(map(int, input("Последовательность (через пробел): ").split()))
max_count = 1
current_count = 1
for i in range(1, len(seq)):
    if seq[i] == seq[i-1]:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 1
print(f"Наибольшее количество подряд идущих одинаковых элементов: {max_count}")