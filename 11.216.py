grades = list(map(int, input("Оценки: ").split()))
count = 0
for grade in grades:
    count += (grade == 5)
    if grade != 5:
        break
print("Количество пятерок:", count)