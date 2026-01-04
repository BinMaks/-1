n = int(input("Количество спортсменов: "))
results = [float(input(f"Результат {i+1}-го спортсмена (сотые доли сек): ")) for i in range(n)]
sorted_results = sorted(results)
team_indices = [results.index(sorted_results[i]) + 1 for i in range(4)]
team_sum = sum(sorted_results[:4])
print(f"Номера бегунов: {team_indices}")
print(f"Суммарное время: {team_sum:.2f} сек")