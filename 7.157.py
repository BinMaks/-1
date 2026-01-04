n = int(input("Введите количество чисел: "))
a = [int(input(f"a[{i+1}] = ")) for i in range(n)]
max_val = max(a)
max_idx = len(a) - a[::-1].index(max_val)
min_val = min(a)
min_idx = a.index(min_val)
print(f"Номер максимального числа: {max_idx}")
print(f"Номер минимального числа: {min_idx + 1}")