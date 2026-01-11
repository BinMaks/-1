import random

print("10.5. 30 чисел (0–5), выводим только нечётные:")
for _ in range(30):
    num = random.randint(0, 5)
    if num % 2 == 1:
        print(num, end=" ")
print()