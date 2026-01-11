scores = []
for i in range(3):
    print(f"Группа {i+1}:")
    group_scores = []
    for _ in range(20):
        exam1 = float(input("Экзамен 1: "))
        exam2 = float(input("Экзамен 2: "))
        exam3 = float(input("Экзамен 3: "))
        avg = (exam1 + exam2 + exam3) / 3
        group_scores.append(avg)
    scores.append(sum(group_scores) / 20)
best_group = scores.index(max(scores)) + 1
print(f"Лучшая группа: {best_group} со средним баллом {max(scores):.2f}")