m = int(input("Введите m: "))
b = int(input("Введите b: "))
a = [int(input(f"a[{i}]: ")) for i in range(m)]
count_greater_b = sum(1 for ai in a if ai > b)
print("Количество чисел > b кратно целому числу b" if count_greater_b % b == 0 else "Количество чисел > b не кратно целому числу b")