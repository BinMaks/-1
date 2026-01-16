rain_months = [float(x) for x in input("Осадки за каждый месяц года (12 месяцев): ").split()]
total_rain = sum([rain_months[2], rain_months[5], rain_months[8], rain_months[11]])
print(f"Общее число осадков: {total_rain}")