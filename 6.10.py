correct_password = 1234
while True:
    password = int(input("Введите пароль: "))
    if password == correct_password:
        print("Приветствие: Добро пожаловать!")
        break
    else:
        print("Ошибка: неверный пароль. Попробуйте еще раз.")