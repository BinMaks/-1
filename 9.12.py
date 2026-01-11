students = []
print("Введите количество учеников для 11 параллелей (по 4 класса):")
for i in range(11):
    print(f"Параллель {i + 1}:")
    row = []
    for j in range(4):
        count = int(input(f"Класс {'АБВГ'[j]}: "))
        row.append(count)
    students.append(row)
min_class = min(min(row) for row in students)
print(f"Самый малочисленный класс: {min_class} учеников")
min_parallel = min(sum(row) for row in students)
print(f"Минимальное количество учеников в параллели: {min_parallel}")
min_A = min(students[i][0] for i in range(11))
min_B = min(students[i][1] for i in range(11))
min_V = min(students[i][2] for i in range(11))
min_G = min(students[i][3] for i in range(11))
print(f"Минимальное количество учеников:")
print(f"Класс А: {min_A}")
print(f"Класс Б: {min_B}")
print(f"Класс В: {min_V}")
print(f"Класс Г: {min_G}")