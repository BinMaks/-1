rain = [float(x) for x in input("Осадки за каждый день августа: ").split()]
rainy_days = [x for x in rain if x > 0]
if rainy_days:
    avg_rain = sum(rainy_days) / len(rainy_days)
    print(f"Среднее количество осадков в дождливые дни: {avg_rain}")
else:
    print("Дождливых дней не было")