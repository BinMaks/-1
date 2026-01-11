grades = []
print("Введите оценки для 12 учеников по 3 предметам (по строкам):")
for i in range(12):
    row = []
    for j in range(3):
        grade = int(input(f"Ученик {i+1}, предмет {j+1}: "))
        row.append(grade)
    grades.append(row)
total_sum = sum(sum(row) for row in grades)
print(f"Сумма всех оценок: {total_sum}")