grades = [int(input(f"Оценка по предмету {i+1}: ")) for i in range(12)]
has_threes = 3 in grades
print("Среди оценок есть тройки" if has_threes else "Среди оценок нет троек")