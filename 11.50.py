september_rain = [float(x) for x in input("Осадки за каждый день сентября (30 дней): ").split()]
avg1 = sum(september_rain[:10]) / 10
avg2 = sum(september_rain[10:20]) / 10
avg3 = sum(september_rain[20:]) / 10
print(f"Среднее за 1-ю декаду: {avg1:.2f} мм")
print(f"Среднее за 2-ю декаду: {avg2:.2f} мм")
print(f"Среднее за 3-ю декаду: {avg3:.2f} мм")