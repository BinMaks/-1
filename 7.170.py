n = int(input("Количество чисел (≥3): "))
x = [int(input(f"x[{i+1}] = ")) for i in range(n)]
max_sum = -float('inf')
min_sum = float('inf')
max_pair_idx = (0, 0)
min_pair_idx = (0, 0)
for i in range(n - 1):
    pair_sum = x[i] + x[i + 1]
    if pair_sum > max_sum:
        max_sum = pair_sum
        max_pair_idx = (i + 1, i + 2)
    if pair_sum < min_sum:
        min_sum = pair_sum
        min_pair_idx = (i + 1, i + 2)
print(f"а) Максимальная сумма двух соседних чисел: {max_sum}")
print(f"б) Минимальная сумма двух соседних чисел: {min_sum}")
print(f"в) Номера чисел с макс. суммой: {max_pair_idx}")
print(f"г) Номера чисел с мин. суммой: {min_pair_idx}")