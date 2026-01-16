grades = list(map(int, input("28 оценок по информатике: ").split()))
has_two = False
for grade in grades:
    if grade == 2:
        has_two = True
        break
if has_two:
    print("Среди оценок есть двойки.")
else:
    print("Среди оценок нет двоек.")