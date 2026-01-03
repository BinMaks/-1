
rainfall = [int(input(f"Осадки за день {i+1} марта: ")) for i in range(31)]
no_rain_days = sum(1 for day in rainfall if day == 0)
print("Осадков не было ровно 10 дней" if no_rain_days == 10 else "Осадков не было не ровно 10 дней")