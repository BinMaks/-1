june_rain = [float(x) for x in input("Осадки за каждый день июня (30 дней): ").split()]
decade1 = sum(june_rain[:10])
decade2 = sum(june_rain[10:20])
decade3 = sum(june_rain[20:])
print(f"Осадки за 1-ю декаду: {decade1} мм")
print(f"Осадки за 2-ю декаду: {decade2} мм")
print(f"Осадки за 3-ю декаду: {decade3} мм")