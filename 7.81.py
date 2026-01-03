wins = 0
draws = 0
losses = 0
total_points = 0
for i in range(20):
    game_result = int(input(f"Результат игры {i+1} (например, 32 для 3 забитых и 2 пропущенных): "))
    goals_scored = game_result // 10
    goals_conceded = game_result % 10
    if goals_scored > goals_conceded:
        wins += 1
        total_points += 3
    elif goals_scored == goals_conceded:
        draws += 1
        total_points += 1
    else:
        losses += 1
print(f"Выигрышей: {wins}")
print(f"Ничьих: {draws}")
print(f"Проигрышей: {losses}")
print(f"Общее число очков: {total_points}")