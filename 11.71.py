grades = [int(x) for x in input("Оценки 25 учеников по химии: ").split()]
failing_students = sum(1 for grade in grades if grade < 3)
print(f"Количество неуспевающих учеников: {failing_students}")