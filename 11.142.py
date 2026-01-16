
scores = list(map(int, input("Введите очки 20 команд: ").split()))
scores_sorted = sorted(scores, reverse=True)
print(f"Первое место по очкам: {scores_sorted[0]}, второе место: {scores_sorted[1]}")