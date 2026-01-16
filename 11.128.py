temperatures = list(map(float, input("Средние температуры за 31 день июля: ").split()))
min_temp = min(temperatures)
count = temperatures.count(min_temp)
print(f"Количество самых прохладных дней: {count}")