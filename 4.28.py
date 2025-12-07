num = int(input("Двузначное число: "))
a = int(input("Число a: "))
sum_digits = num // 10 + num % 10
if 10 <= sum_digits <= 99:
    print("Сумма цифр - двузначное число")
else:
    print("Сумма цифр не двузначна")

if sum_digits > a:
    print("Сумма цифр больше a")
elif sum_digits < a:
    print("Сумма цифр меньше a")
else:
    print("Сумма цифр равна a")