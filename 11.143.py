
temperatures = list(map(float, input("Введите температуры за 31 день июля: ").split()))
temp_with_index = [(temp, i+1) for i, temp in enumerate(temperatures)]
temp_sorted = sorted(temp_with_index, reverse=True)
print(f"Самые тёплые дни: {temp_sorted[0][1]}")