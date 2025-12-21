
while True:
    num = int(input("Введите четное число: "))
    if num % 2 == 0:
        print("Верно!")
        break
    else:
        print("Ошибка: число нечетное. Попробуйте еще раз.")