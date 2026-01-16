temperatures = list(map(float, input("Введите температуры за 28 дней февраля: ").split()))
temp_with_index = [(temp, i+1) for i, temp in enumerate(temperatures)]
temp_sorted = sorted(temp_with_index)
print(f"Самые холодные дни: {temp_sorted[0][1]}")