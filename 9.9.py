scores = []
print("Введите баллы для 8 спортсменов (по 5 видам спорта):")
for i in range(8):
    print(f"Спортсмен {i + 1}:")
    row = []
    for j in range(5):
        score = int(input(f"Вид спорта {j + 1}: "))
        row.append(score)
    scores.append(row)
max_score = max(max(row) for row in scores)
print(f"Максимальная оценка в таблице: {max_score}")
total_scores = [sum(row) for row in scores]
max_total = max(total_scores)
winner_index = total_scores.index(max_total)
print(f"Сумма баллов победителя: {max_total}")
print(f"Победитель — спортсмен №{winner_index + 1}")