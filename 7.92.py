grades = [int(input(f"Оценка {i+1} ученика: ")) for i in range(28)]
has_twos = 2 in grades
print("Среди оценок есть двойки" if has_twos else "Среди оценок нет двоек")