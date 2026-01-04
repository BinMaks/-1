n = int(input("Количество спортсменов: "))
times = [float(input(f"Время {i+1}-го спортсмена: ")) for i in range(n)]
best_time = min(times)
best_athlete = times.index(best_time) + 1
print(f"Лыжник с лучшим результатом стартовал {best_athlete}-м")