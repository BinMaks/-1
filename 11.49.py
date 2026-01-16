february_rain = [float(x) for x in input("Осадки за каждый день февраля (28 дней): ").split()]
avg_rain = sum(february_rain) / len(february_rain)
print(f"Среднедневное количество осадков: {avg_rain:.2f} мм")