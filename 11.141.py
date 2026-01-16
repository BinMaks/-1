
birth_years = list(map(int, input("Введите годы рождения 30 человек: ").split()))
birth_years_sorted = sorted(birth_years)
print(f"Два самых старших по возрасту: {birth_years_sorted[0]} и {birth_years_sorted[1]}")