
a = float(input("Введите a: "))
n = 2
while 1 + 1 / n >= a:
    n += 1
print(f"Наименьшее n, при котором 1 + 1/n < {a}: {n}")