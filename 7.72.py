n = int(input("Количество чисел: "))
numbers = [float(input(f"Число {i+1}: ")) for i in range(n)]
count_negative = sum(1 for x in numbers if x < 0)
count_positive = sum(1 for x in numbers if x > 0)
print("Количество отрицательных чисел:", count_negative)
print("Количество положительных чисел:", count_positive)