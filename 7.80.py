wins = 0
losses = 0
draws = 0
games_with_diff_3 = 0
total_points = 0
for i in range(20):
    goals_scored, goals_conceded = map(int, input(f"Игра {i+1} (забитые, пропущенные): ").split())
    diff = goals_scored - goals_conceded
    if goals_scored > goals_conceded:
        result = "выигрыш"
        wins += 1
        total_points += 3
    elif goals_scored < goals_conceded:
        result = "проигрыш"
        losses += 1
    else:
        result = "ничья"
        draws += 1
        total_points += 1
    print(f"Игра {i+1}: {result}")
    if diff >= 3:
        games_with_diff_3 += 1
print(f"Выигрышей: {wins}")
print(f"Проигрышей: {losses}")
print(f"Ничьих: {draws}")
print(f"Игр с разницей ≥3: {games_with_diff_3}")
print(f"Общее число очков: {total_points}")