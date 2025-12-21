count = 0
while count < 10:
    num = int(input("Введите число (0 для остановки): "))
    if num == 0:
        print("Ввод прекращен.")
        break
    print("Введено число:", num)
    count += 1
if count < 10:
    print("Ввод завершен досрочно.")
else:
    print("Введено 10 чисел.")