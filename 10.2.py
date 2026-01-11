import random
print("а) 10 случайных целых чисел (0–10):")
for _ in range(10):
    print(random.randint(0, 10))
k = int(input("\nб) Введите k: "))
a = int(input("Введите a: "))
print(f"{k} случайных целых чисел (0–{a}):")
for _ in range(k):
    print(random.randint(0, a))
print("\nв) 20 случайных целых чисел (10–20):")
for _ in range(20):
    print(random.randint(10, 20))
k = int(input("\nг) Введите k: "))
a = int(input("Введите a: "))
print(f"{k} случайных целых чисел (-10–{a}):")
for _ in range(k):
    print(random.randint(-10, a))
a = int(input("\nд) Введите a: "))
b = int(input("Введите b: "))
k = random.randint(1, 15)
print(f"{k} случайных целых чисел ({a}–{b}):")
for _ in range(k):
    print(random.randint(a, b))