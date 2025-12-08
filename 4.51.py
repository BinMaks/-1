num = int(input("Введите трехзначное число: "))
n = int(input("Введите цифру n: "))
if '6' in str(num):
    print("цифра 6 входит в число")
else:
    print("Цифра 6 не входит в число")
if str(n) in str(num):
    print(f"Цифра {n} входит в число")
else:
    print(f"Цифра {n} не входит в число")
