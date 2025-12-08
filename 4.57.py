a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = int(input("Введите d: "))
remainder = a % b
if remainder == c or remainder == d:
    print("Остаток равен c или d")
else:
    print("остоаток не равен ни c, ни d")