
temps = [float(input(f"Температура {i+1}-го дня: ")) for i in range(30)]
min_temp = min(temps)
cold_days = temps.count(min_temp)
print(f"Самая низкая температура ({min_temp}°C) была {cold_days} дней")