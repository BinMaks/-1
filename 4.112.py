a, b, c = map(int, input("Введите три числа: ").split())
sum_pos = 0
if a > 0: sum_pos += a
if b > 0: sum_pos += b
if c > 0: sum_pos += c
print(f"Сумма положительных: {sum_pos}")