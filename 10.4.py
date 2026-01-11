import random

print("10.4. 50 чисел (0–3), выводим только 0 и 1:")
for _ in range(50):
    num = random.randint(0, 3)
    if num in [0, 1]:
        print(num, end=" ")
print()