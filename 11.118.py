birth_years = list(map(int, input("Введите год рождения 30 человек: ").split()))
max_year = max(birth_years)
min_year = min(birth_years)
age_diff = max_year - min_year
print(f"Разница в возрасте: {age_diff} лет")