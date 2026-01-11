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
print(f"Численность самого малочисленного класса: {min_class} учеников")