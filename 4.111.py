a, b, c, d = map(int, input("Введите четыре числа: ").split())
count = 0
if a % 2 == 0: count += 1
if b % 2 == 0: count += 1
if c % 2 == 0: count += 1
if d % 2 == 0: count += 1
print(f"Количество чётных: {count}")