rain = [float(x) for x in input("Осадки за каждый день января: ").split()]
avg_rain = sum(rain) / len(rain)
rainy_days = [i+1 for i, r in enumerate(rain) if r > avg_rain]
print(f"Дни с осадками > средних: {rainy_days}")