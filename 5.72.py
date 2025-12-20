import math
n = int(input("Введите n: "))
sum_sin = 0
total_a = 0
for i in range(1, n + 1):
    sum_sin += math.sin(i)
    total_a += 1 / sum_sin
print(f"Результат (a): {total_a:.6f}")
result_b = 2
for _ in range(n):
    result_b = math.sqrt(result_b)
print(f"Результат (б): {result_b:.6f}")
sum_cos = 0
sum_sin = 0
total_c = 0
for i in range(1, n + 1):
    sum_cos += math.cos(i)
    sum_sin += math.sin(i)
    total_c += sum_cos / sum_sin
print(f"Результат (в): {total_c:.6f}")
total_d = 0
for i in range(1, n + 1):
    total_d += 3 * i
print(f"Результат (г): {total_d}")