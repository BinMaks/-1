rain_june = [float(x) for x in input("Осадки за каждый день июня (30 дней): ").split()]
first_half = sum(rain_june[:15])
second_half = sum(rain_june[15:])

if first_half > second_half:
    print("В первой половине июня выпало больше осадков")
elif second_half > first_half:
    print("Во второй половине июня выпало больше осадков")
else:
    print("Осадков выпало поровну")

decade1 = sum(rain_june[:10])
decade2 = sum(rain_june[10:20])
decade3 = sum(rain_june[20:])
max_decade = max(decade1, decade2, decade3)
if max_decade == decade1:
    print("Больше всего осадков выпало в 1-й декаде")
elif max_decade == decade2:
    print("Больше всего осадков выпало во 2-й декаде")
else:
    print("Больше всего осадков выпало в 3-й декаде")