x = [float(input(f"x[{i}]: ")) for i in range(15)]
count_not_more_33_2 = sum(1 for xi in x if xi <= 33.2)
print("Количество чисел ≤ 33.2 кратно 4" if count_not_more_33_2 % 4 == 0 else "Количество чисел ≤ 33.2 не кратно 4")