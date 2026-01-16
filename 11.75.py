results = [int(x) for x in input("Результаты 20 игр (3 — выигрыш, 0 — проигрыш, 1 — ничья): ").split()]
wins = sum(1 for r in results if r == 3)
draws = sum(1 for r in results if r == 1)
print(f"Выигрышей: {wins}, ничьих: {draws}")