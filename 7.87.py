m = int(input("Введите m: "))
d = [int(input(f"d[{i}]: ")) for i in range(m)]
count_positive = sum(1 for di in d if di > 0)
print("Количество положительных чисел кратно 3" if count_positive % 3 == 0 else "Количество положительных чисел не кратно 3")