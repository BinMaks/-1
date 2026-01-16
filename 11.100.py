grades = [float(x) for x in input("Оценки 22 учеников: ").split()]
avg_grade = sum(grades) / len(grades)
low_grades = [i+1 for i, g in enumerate(grades) if g < avg_grade]
print(f"Номера учеников с оценками < средней: {low_grades}")