scores = list(map(int, input("Заброшенные мячи (15 игр): ").split()))
missed = list(map(int, input("Пропущенные мячи (15 игр): ").split()))
for i in range(15):
    if scores[i] > missed[i]:
        print(f"Игра {i+1}: выигрыш")
    else:
        print(f"Игра {i+1}: проигрыш")