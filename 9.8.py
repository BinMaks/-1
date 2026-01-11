grades = []
print("Введите оценки для 14 студентов (по 3 предметам):")
for i in range(14):
    print(f"Студент {i + 1}:")
    row = []
    for j in range(3):
        grade = int(input(f"Предмет {j + 1}: "))
        row.append(grade)
    grades.append(row)
count_no_twos = 0
for student in grades:
    if 2 not in student:
        count_no_twos += 1
print(f"Количество студентов, сдавших без двоек: {count_no_twos}")
count_only_4_5 = 0
for j in range(3):
    subject_grades = [grades[i][j] for i in range(14)]
    if all(grade in [4, 5] for grade in subject_grades):
        count_only_4_5 += 1
print(f"Количество предметов с оценками только '5' и '4': {count_only_4_5}")
twos_per_subject = [0, 0, 0]
for j in range(3):
    for i in range(14):
        if grades[i][j] == 2:
            twos_per_subject[j] += 1
print("Количество двоек по предметам:")
for j, count in enumerate(twos_per_subject, 1):
    print(f"Предмет {j}: {count}")