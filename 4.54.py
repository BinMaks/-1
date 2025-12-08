num = int(input("Введите четырехзначное число: "))
b = int(input("Введите цифру b: "))
if '4' in str(num):
    print("Цифра 4 входит в число")
else:
    print("Цифра 4 не входит в число")
if str(b) in str(num):
    print(f"Цифра {b} входит в число")
else:
    print(f"Цифра {b} не входит в число")