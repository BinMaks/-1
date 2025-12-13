n = int(input("Введите возраст (1–99): "))
if 10 <= n % 100 <= 20:
    suffix = "лет"
elif n % 10 == 1:
    suffix = "год"
elif 2 <= n % 10 <= 4:
    suffix = "года"
else:
    suffix = "лет"
print(f"Мне {n} {suffix}.")