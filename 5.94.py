n = int(input("Введите число n: "))
i = 1
while True:
    if i * i > n:
        break
    print(i)
    i += 1