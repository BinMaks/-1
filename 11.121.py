rainfall = list(map(float, input("Осадки за 31 день июля: ").split()))
max_rain = max(rainfall)
first_rainy = rainfall.index(max_rain) + 1
print(f"Первый самый дождливый день: {first_rainy}")
last_rainy = len(rainfall) - rainfall[::-1].index(max_rain)
print(f"Последний самый дождливый день: {last_rainy}")