n = int(input("Количество студентов: "))
exam1 = [int(input(f"Оценка {i+1} студента на первом экзамене: ")) for i in range(n)]
exam2 = [int(input(f"Оценка {i+1} студента на втором экзамене: ")) for i in range(n)]
count_twos = sum(1 for i in range(n) if exam1[i] == 2 or exam2[i] == 2)
print("Количество студентов с двойкой:", count_twos)