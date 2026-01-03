m = int(input("Количество чисел: "))
numbers = [int(input(f"Число {i+1}: ")) for i in range(m)]
count_div3 = sum(1 for x in numbers if x % 3 == 0)
count_div7 = sum(1 for x in numbers if x % 7 == 0)
print("Количество чисел, кратных 3:", count_div3)
print("Количество чисел, кратных 7:", count_div7)