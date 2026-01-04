days = 30
precipitation = [float(input(f"Осадки за день {i+1}: ")) for i in range(days)]
max_precipitation = max(precipitation)
last_day = len(precipitation) - precipitation[::-1].index(max_precipitation)
print(f"Дата последнего дня с максимальным количеством осадков: {last_day}")