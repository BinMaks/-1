grades = [int(input(f"Оценка {i+1}: ")) for i in range(30)]
count_fives = grades.count(5)
count_fours = grades.count(4)
count_threes = grades.count(3)
count_twos = grades.count(2)

print("Пятёрок:", count_fives)
print("Четвёрок:", count_fours)
print("Троек:", count_threes)
print("Двоек:", count_twos)