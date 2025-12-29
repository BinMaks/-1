a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
power = 1
while power <= b:
    if power >= a:
        print(power, end=" ")
    power *= 2