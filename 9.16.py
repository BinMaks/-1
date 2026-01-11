students = []
print("Введите количество студентов для 5 курсов (по 6 групп):")
for i in range(5):
    print(f"Курс {i + 1}:")
    row = []
    for j in range(6):
        count = int(input(f"Группа {j + 1}: "))
        row.append(count)
    students.append(row)
total_per_course = [sum(row) for row in students]
min_course = total_per_course.index(min(total_per_course)) + 1
min_students = min(total_per_course)
print(f"\nКурс с наименьшим количеством студентов: {min_course} (всего {min_students} студентов)")
all_groups = [(i + 1, j + 1, students[i][j]) for i in range(5) for j in range(6)]
min_group = min(all_groups, key=lambda x: x[2])
print(f"Самая малочисленная группа: курс {min_group[0]}, группа {min_group[1]} ({min_group[2]} студентов)")

for i, row in enumerate(students, 1):
    min_group_num = row.index(min(row)) + 1
    min_count = min(row)
    print(f"На курсе {i} самая малочисленная группа — {min_group_num} ({min_count} студентов)")