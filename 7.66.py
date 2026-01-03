n = int(input("Введите n: "))
numbers = [float(input(f"Число {i+1}: ")) for i in range(n)]
count_negative = sum(1 for x in numbers if x < 0)
print("Количество отрицательных чисел в начале:", count_negative)