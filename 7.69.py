grades = [int(input(f"Оценка {i+1}: ")) for i in range(20)]
count_fives = grades.count(5)
print("Количество пятёрок:", count_fives)