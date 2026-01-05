a = float(input("Введите a: "))
n = 1
while True:
    current = 1 + 1 / n
    if current < a:
        print(current)
        n += 1
    else:
        break