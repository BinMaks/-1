birth_year = int(input("Год рождения: "))
birth_month = int(input("Месяц рождения (1–12): "))
current_year = int(input("Текущий год: "))
current_month = int(input("Текущий месяц (1–12): "))
years = current_year - birth_year
if current_month >= birth_month:
    months = current_month - birth_month
else:
    years -= 1
    months = 12 - birth_month + current_month
print(f"Возраст: {years} лет и {months} месяцев")