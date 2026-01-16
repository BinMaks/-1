
times = list(map(float, input("Введите результаты 23 спортсменов (в сотых долях сек.): ").split()))
from itertools import combinations
best_team = min(combinations(times, 4), key=sum)
print(f"Команда из 4 лучших бегунов: {list(best_team)}, суммарное время: {sum(best_team)}")