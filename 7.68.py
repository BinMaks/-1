
n = int(input("Количество чисел: "))
sequence = [int(input(f"Число {i+1}: ")) for i in range(n)]
first_num = sequence[0]
count_equal = sum(1 for x in sequence if x == first_num)
print("Количество равных элементов в начале:", count_equal)