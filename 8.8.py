a = float(input("Введите a: "))
n = 2
results = []
while 1 + 1 / n >= a:
    results.append(n)
    n += 1
print(f"Значения n, при которых числа не меньше {a}: {results}")