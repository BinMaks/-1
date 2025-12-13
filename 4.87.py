print("Данные первого человека:")
birth_year1 = int(input("Год рождения: "))
birth_month1 = int(input("Месяц рождения (1–12): "))
birth_day1 = int(input("День рождения (1–31): "))
print("Данные второго человека:")
birth_year2 = int(input("Год рождения: "))
birth_month2 = int(input("Месяц рождения (1–12): "))
birth_day2 = int(input("День рождения (1–31): "))
if (birth_year1, birth_month1, birth_day1) < (birth_year2, birth_month2, birth_day2):
    print("Первый человек старше.")
elif (birth_year1, birth_month1, birth_day1) > (birth_year2, birth_month2, birth_day2):
    print("Второй человек старше.")
else:
    print("Они ровесники.")