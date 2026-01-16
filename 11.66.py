rain_feb = [float(x) for x in input("Осадки за каждый день февраля (28 дней): ").split()]

sum_even_days = sum(rain_feb[i] for i in range(1, 28, 2))

sum_odd_days = sum(rain_feb[i] for i in range(0, 28, 2))

if sum_even_days > sum_odd_days:
    print("Больше осадков выпало в четные дни")
elif sum_odd_days > sum_even_days:
    print("Больше осадков выпало в нечетные дни")
else:
    print("Осадков выпало поровну")