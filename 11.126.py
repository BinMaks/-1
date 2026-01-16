
rainfall = list(map(float, input("Осадки за 31 день октября: ").split()))
max_rain = max(rainfall)
count = rainfall.count(max_rain)
print(f"Дней с максимальным количеством осадков: {count}")