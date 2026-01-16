goals = list(map(int, input("Забитые мячи (20 игр): ").split()))
missed = list(map(int, input("Пропущенные мячи (20 игр): ").split()))
for i in range(20):
    if goals[i] > missed[i]:
        print(f"Игра {i+1}: выигрыш")
    elif goals[i] == missed[i]:
        print(f"Игра {i+1}: ничья")
    else:
        print(f"Игра {i+1}: проигрыш")