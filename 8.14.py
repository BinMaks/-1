
a = float(input("Введите a (0 < a <= 1): "))
n = 1
while 1 / n >= a:
    n += 1
print(f"Первое число, меньшее {a}: {1 / n}")