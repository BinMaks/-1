import random
print("а) 8 случайных чисел (0 < n_i < 1):")
for _ in range(8):
    print(round(random.uniform(0, 1), 2))
k = int(input("\nб) Введите k: "))
print(f"{k} случайных чисел (0 < n_i < 1):")
for _ in range(k):
    print(round(random.uniform(0, 1), 2))
print("\nв) 15 случайных чисел (25 ≤ n_i < 26):")
for _ in range(15):
    print(round(random.uniform(25, 26), 2))
print("\nг) 20 случайных чисел (0 ≤ n_i < 15):")
for _ in range(20):
    print(round(random.uniform(0, 15), 2))
a = int(input("\nд) Введите a: "))
b = int(input("Введите b: "))
k = random.randint(1, a)
print(f"{k} случайных чисел (0 ≤ n_i < {b}):")
for _ in range(k):
    print(round(random.uniform(0, b), 2))
print("\nе) 10 случайных чисел (-40 ≤ n_i < 40):")
for _ in range(10):
    print(round(random.uniform(-40, 40), 2))
m = int(input("\nж) Введите m: "))
a = int(input("Введите a: "))
b = int(input("Введите b: "))
k = random.randint(1, m)
print(f"{k} случайных чисел ({a} ≤ n_i < {b}):")
for _ in range(k):
    print(round(random.uniform(a, b), 2))