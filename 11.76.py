grades = [int(x) for x in input("Оценки ученика по 10 предметам: ").split()]
good_grades = sum(1 for g in grades if g in [4, 5])
print(f"Четверок и пятерок: {good_grades}")