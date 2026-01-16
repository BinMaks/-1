temperatures = list(map(float, input("Введите температуры за июль (31 день): ").split()))
max_sum = float('-inf')
best_start_day = 0
for i in range(len(temperatures) - 6):
    current_sum = sum(temperatures[i:i+7])
    if current_sum > max_sum:
        max_sum = current_sum
        best_start_day = i
print(f"Самые теплые 7 дней начинаются с {best_start_day + 1}-го дня")
print(f"Среднесуточная температура: {max_sum / 7:.2f}")