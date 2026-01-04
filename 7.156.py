def get_max_monotonic_length():
    seq = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
    max_length = 1
    current_length = 1

    for i in range(1, len(seq)):
        if seq[i] > seq[i-1] or seq[i] < seq[i-1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    return max_length

print("Наибольшая длина монотонного фрагмента:", get_max_monotonic_length())