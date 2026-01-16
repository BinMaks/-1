birth_years = list(map(int, input("Годы рождения 30 человек: ").split()))
min_year = min(birth_years)
first_oldest = birth_years.index(min_year) + 1
print(f"Первый самый старший (номер): {first_oldest}")
last_oldest = len(birth_years) - birth_years[::-1].index(min_year)
print(f"Последний самый старший (номер): {last_oldest}")