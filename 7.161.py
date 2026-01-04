
n = int(input("Количество команд: "))
scores = [int(input(f"Очки {i+1}-й команды: ")) for i in range(n)]
min_score = min(scores)
min_team = scores.index(min_score) + 1
print(f"Команда с наименьшим количеством очков: {min_team}")