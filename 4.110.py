a, b, c, d = map(float, input("Введите четыре числа: ").split())
count = 0
if a < 0: count += 1
if b < 0: count += 1
if c < 0: count += 1
if d < 0: count += 1
print(f"Количество отрицательных: {count}")