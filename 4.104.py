import math
a, b = map(float, input("Введите два числа: ").split())
abs_a = a if a >= 0 else -a
abs_b = b if b >= 0 else -b
semi_sum = (abs_a + abs_b) / 2
sqrt_prod = math.sqrt(abs_a * abs_b)
print(f"Полусумма: {semi_sum}, корень из произведения: {sqrt_prod}")
