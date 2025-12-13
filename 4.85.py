n = int(input("Введите возраст в месяцах (1–1188): "))
years = n // 12
months = n % 12
if months == 0:
    print(f"{years} лет ровно")
else:
    print(f"{years} лет {months} месяцев")