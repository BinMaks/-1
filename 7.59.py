grades = [int(input(f"Оценка {i+1}-го ученика: ")) for i in range(int(input("Количество учеников: ")))]
count_fives = sum(1 for grade in grades if grade == 5)
print("Количество пятёрок:", count_fives)