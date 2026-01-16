wins = [int(x) for x in input("Количество побед 20 команд: ").split()]
weak_teams = [i + 1 for i, x in enumerate(wins) if x < 3]
print("Команды с менее чем 3 победами:", weak_teams)