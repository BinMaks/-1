import random
a = int(input("Введите a: "))
b = int(input("Введите b: "))
m = random.randint(1, 20)
n = random.randint(1, 20)
print(f"m = {m}, n = {n}")
print(f"{n} целых чисел в диапазоне [{a}, {b}]:")
for _ in range(n):
    print(random.randint(a, b))
print(f"{m} неотрицательных вещественных чисел (≤ {n}):")
for _ in range(m):
    print(round(random.uniform(0, n), 2))