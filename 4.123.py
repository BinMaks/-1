points = int(input("Введите количество очков: "))
if points == 3:
    print("Результат игры: выигрыш")
elif points == 1:
    print("Результат игры: ничья")
elif points == 0:
    print("Результат игры: проигрыш")
else:
    print("Некорректное количество очков")