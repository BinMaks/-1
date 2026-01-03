n = int(input("Количество команд: "))
wins_losses = [[int(input(f"Выигрыши {i+1}-й команды: ")), int(input(f"Проигрыши {i+1}-й команды: "))] for i in range(n)]
count_more_wins = sum(1 for wins, losses in wins_losses if wins > losses)
print("Команд с больше выигрышей, чем проигрышей:", count_more_wins)