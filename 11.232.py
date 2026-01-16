goals = list(map(int, input("Забитые мячи (20 игр): ").split()))
missed = list(map(int, input("Пропущенные мячи (20 игр): ").split()))
for i in range(20):
    if goals[i] > missed[i]:
        print(f"Игра {i+1}: выигрыш")
    elif goals[i] == missed[i]:
        print(f"Игра {i+1}: ничья")
    else:
        print(f"Игра {i+1}: проигрыш")
wins = sum(1 for i in range(20) if goals[i] > missed[i])
print(f"Количество выигрышей: {wins}")
losses = sum(1 for i in range(20) if goals[i] < missed[i])
print(f"Количество выигрышей: {wins}, проигрышей: {losses}")
draws = sum(1 for i in range(20) if goals[i] == missed[i])
print(f"Выигрыши: {wins}, ничьи: {draws}, проигрыши: {losses}")
big_diff = sum(1 for i in range(20) if abs(goals[i] - missed[i]) >= 3)
print(f"Игр с разницей ≥ 3: {big_diff}")
points = 3 * wins + draws
print(f"Набрано очков: {points}")