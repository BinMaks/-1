rain_feb = [int(x) for x in input("Осадки за каждый день февраля (28 дней): ").split()]
no_rain_days = sum(1 for x in rain_feb if x == 0)
print(f"Дней без осадков: {no_rain_days}")