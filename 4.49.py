num = int(input("Введите двузначное число: "))
a = int(input("Введите цифру a: "))
if '3' in str(num):
    print("Цифра 3 входит в число: ")
else:
    print("Цифра 3 не входит в число")
if str(a) in str(num):
    print(f"Цифра {a} входит в число")
else:
    print(f"Цифра {a} не входит в число")