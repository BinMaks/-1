rain = [float(x) for x in input("Осадки за 15 лет: ").split()]
avg_rain = sum(rain) / len(rain)
deviations = [r - avg_rain for r in rain]
print(f"Среднее количество осадков: {avg_rain}")
print("Отклонения для каждого года:")
for i, dev in enumerate(deviations):
    print(f"Год {i+1}: {dev}")