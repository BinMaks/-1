
results = list(map(float, input("Введите результаты 22 спортсменов: ").split()))
results_sorted = sorted(results)
print(f"Первое место: {results_sorted[0]}, второе место: {results_sorted[1]}")