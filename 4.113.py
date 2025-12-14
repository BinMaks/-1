
a, b, c, d = map(float, input("Введите четыре числа: ").split())
sum_greater_5 = 0
if a > 5: sum_greater_5 += a
if b > 5: sum_greater_5 += b
if c > 5: sum_greater_5 += c
if d > 5: sum_greater_5 += d
print(f"Сумма чисел > 5: {sum_greater_5}")