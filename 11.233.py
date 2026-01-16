games = list(map(int, input("Результаты 20 игр (двузначные числа): ").split()))
wins = 0
losses = 0
draws = 0
points = 0
for game in games:
    goals = game // 10
    missed = game % 10
    if goals > missed:
        result = "выигрыш"
        wins += 1
        points += 3
    elif goals == missed:
        result = "ничья"
        draws += 1
        points += 1
    else:
        result = "проигрыш"
        losses += 1
    print(f"Игра: {goals}-{missed}, результат: {result}")
print(f"Выигрыши: {wins}, ничьи: {draws}, проигрыши: {losses}")
print(f"Набрано очков: {points}")