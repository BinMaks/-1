n = int(input("Количество игр: "))
wins = 0
losses = 0
draws = 0

for _ in range(n):
    points = int(input("Очки за игру (3 — победа, 1 — ничья, 0 — поражение): "))
    if points == 3:
        wins += 1
    elif points == 1:
        draws += 1
    else:
        losses += 1

print("Выигрышей:", wins)
print("Проигрышей:", losses)
print("Ничьих:", draws)