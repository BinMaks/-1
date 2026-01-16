rain_feb = [float(x) for x in input("Осадки за каждый день февраля (28 дней): ").split()]
sum_even_days = sum(rain_feb[i] for i in range(1, 28, 2))
print(f"Общее число осадков по четным числам: {sum_even_days}")