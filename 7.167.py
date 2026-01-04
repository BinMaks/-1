n = int(input("Количество чисел: "))
x = [int(input(f"x[{i+1}] = ")) for i in range(n)]

max_val = max(x)
min_val = min(x)
max_idx = x.index(max_val)
min_idx = x.index(min_val)

if max_idx < min_idx:
    print("Максимальное число встречается раньше")
else:
    print("Минимальное число встречается раньше")