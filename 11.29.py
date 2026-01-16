rainfall = [int(x) for x in input("Осадки за каждый день января (31 число): ").split()]
no_rain_days = [i + 1 for i, x in enumerate(rainfall) if x == 0]
print("Дни без осадков:", no_rain_days)