seq = list(map(int, input("Последовательность (через пробел): ").split()))
max_length = 1
current_length = 1

for i in range(1, len(seq)):
    if seq[i] > seq[i-1]:
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 1

print(f"Наибольшая длина монотонно возрастающего фрагмента: {max_length}")