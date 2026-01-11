results = []
print("Введите результаты для 15 спортсменов (по 3 программы):")
for i in range(15):
    print(f"Спортсмен {i + 1}:")
    row = []
    for j in range(3):
        if j == 0:
            score = float(input("Обязательная программа: "))
        elif j == 1:
            score = float(input("Короткая программа: "))
        else:
            score = float(input("Произвольная программа: "))
        row.append(score)
    results.append(row)
print("\nСредние баллы для каждого спортсмена:")
for i, row in enumerate(results, 1):
    avg = sum(row) / 3
    print(f"Спортсмен {i}: {avg:.2f}")
print("\nСредние баллы по каждому виду программы:")
for j in range(3):
    total = sum(results[i][j] for i in range(15))
    avg = total / 15
    if j == 0:
        print(f"Обязательная программа: {avg:.2f}")
    elif j == 1:
        print(f"Короткая программа: {avg:.2f}")
    else:
        print(f"Произвольная программа: {avg:.2f}")