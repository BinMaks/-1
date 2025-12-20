import math
total_sum = 0
for i in range(1, 51):
    total_sum += math.sqrt(i)
print(f"Сумма корней: {total_sum:.6f}")