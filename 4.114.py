a, b, c, d = map(int, input("Введите четыре числа: ").split())
sum_divisible_by_3 = 0
if a % 3 == 0: sum_divisible_by_3 += a
if b % 3 == 0: sum_divisible_by_3 += b
if c % 3 == 0: sum_divisible_by_3 += c
if d % 3 == 0: sum_divisible_by_3 += d
print(f"Сумма кратных трём: {sum_divisible_by_3}")