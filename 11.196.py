grades = list(map(int, input("24 оценки (пятерки в начале): ").split()))
count = 0
for grade in grades:
    if grade == 5:
        count += 1
    else:
        break
print(f"Количество пятерок: {count}")