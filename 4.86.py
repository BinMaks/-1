birth_year = int(input("Год рождения: "))
birth_month = int(input("Месяц рождения (1–12): "))
birth_day = int(input("День рождения (1–31): "))
current_year = int(input("Текущий год: "))
current_month = int(input("Текущий месяц (1–12): "))
current_day = int(input("Текущий день (1–31): "))
age = current_year - birth_year
if (current_month, current_day) < (birth_month, birth_day):
    age -= 1
print(f"Возраст: {age} лет")