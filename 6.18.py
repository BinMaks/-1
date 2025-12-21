import math
a = int(input("Введите a: "))
b = int(input("Введите b: "))
num = a
while num >= b:
    print(math.sqrt(num))
    num -= 1


import math
a = int(input("Введите a: "))
b = int(input("Введите b: "))
num = a
while True:
    print(math.sqrt(num))
    num -= 1
    if num < b:
        break