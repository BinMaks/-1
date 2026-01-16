
rain_march = [int(x) for x in input("Осадки за каждый день марта (31 день): ").split()]
no_rain_days = sum(1 for x in rain_march if x == 0)
print(f"Дней без осадков: {no_rain_days}")
print(f"Осадков не было 10 дней: {no_rain_days == 10}")