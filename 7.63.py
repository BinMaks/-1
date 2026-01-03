chemistry_grades = [int(input(f"Оценка {i+1}-го ученика: ")) for i in range(int(input("Количество учеников: ")))]
count_fives = sum(1 for grade in chemistry_grades if grade == 5)
count_twos = sum(1 for grade in chemistry_grades if grade == 2)
print("Пятёрок:", count_fives, "\nДвоек:", count_twos)