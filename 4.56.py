num = int(input("Введите четырехзначное число: "))
str_num = str(num)
if str_num == str_num[::-1]:
    print("число симметрично")
else:
    print("число не симметрично")