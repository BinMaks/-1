grades = []
print("Введите оценки для 15 учеников (по 3 предметам):")
for i in range(15):
    print(f"Ученик {i + 1}:")
    row = []
    for j in range(3):
        grade = int(input(f"Предмет {j + 1}: "))
        row.append(grade)
    grades.append(row)
fives_count = sum(grades[i][j] == 5 for i in range(15) for j in range(3))
print(f"\nОбщее количество пятёрок: {fives_count}")
print("\nКоличество троек у каждого ученика:")
for i, row in enumerate(grades, 1):
    threes_count = row.count(3)
    print(f"Ученик {i}: {threes_count}")
print("\nКоличество двоек по каждому предмету:")
for j in range(3):
    twos_count = sum(grades[i][j] == 2 for i in range(15))
    print(f"Предмет {j + 1}: {twos_count}")