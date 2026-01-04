m = int(input("Введите количество чисел: "))
d = [int(input(f"d[{i+1}] = ")) for i in range(m)]

max_val = max(d)
max_idx = m - d[::-1].index(max_val)

min_val = min(d)
min_idx = d.index(min_val)

print(f"Номер максимального числа: {max_idx}")
print(f"Номер минимального числа: {min_idx + 1}")