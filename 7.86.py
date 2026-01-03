n = int(input("Введите n: "))
c = [int(input(f"c[{i}]: ")) for i in range(n)]
count_less_20 = sum(1 for ci in c if ci < 20)
print("Количество чисел < 20 равно 5" if count_less_20 == 5 else "Количество чисел < 20 не равно 5")