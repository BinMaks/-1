birth_years = [int(input(f"Год рождения {i+1}-го человека: ")) for i in range(int(input("Количество человек: ")))]
count_before_1990 = sum(1 for year in birth_years if year < 1990)
count_after_2000 = sum(1 for year in birth_years if year > 2000)
print("Родились до 1990 г.:", count_before_1990)
print("Родились после 2000 г.:", count_after_2000)