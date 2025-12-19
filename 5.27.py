total = sum(range(200, 601))
print(f"Сумма: {total}")

a = int(input("Введите a (a < 400): "))
total = sum(range(a, 401))
print(f"Сумма: {total}")


b = int(input("Введите b (b > -15): "))
total = sum(range(-15, b + 1))
print(f"Сумма: {total}")

a = int(input("Введите a: "))
b = int(input("Введите b (b > a): "))
total = sum(range(a, b + 1))
print(f"Сумма: {total}")