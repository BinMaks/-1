a = float(input("Введите a: "))
n = 2
while 1 + 1 / n >= a:
    n += 1
print(f"Первое число, меньшее {a}: 1 + 1/{n} = {1 + 1 / n}")