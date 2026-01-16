results = list(map(float, input("Введите результаты 25 спортсменов: ").split()))
winner_result = min(results)
print(f"Результат победителя: {winner_result}")