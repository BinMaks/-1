birth_year = int(input("Год рождения: "))
birth_month = int(input("Месяц рождения (1-12): "))
current_year = int(input("Текущий год: "))
current_month = int(input("Текущий месяц (1-12): "))
age = current_year - birth_year
if current_month < birth_month:
    age = 1
print(f"Возраст: {age} лет. ")
