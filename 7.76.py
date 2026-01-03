team1_deletions = 0
team2_deletions = 0
team1_time = 0
team2_time = 0

for _ in range(24):
    team, duration = map(int, input("Команда (1/2), длительность (2/5/10): ").split())
    if team == 1:
        team1_deletions += 1
        team1_time += duration
    else:
        team2_deletions += 1
        team2_time += duration

print("Команда 1: удалений —", team1_deletions, ", время —", team1_time)
print("Команда 2: удалений —", team2_deletions, ", время —", team2_time)