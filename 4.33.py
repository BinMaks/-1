num = int(input("трехзначное число"))
a = int(input("Число a: "))
first = num // 100
second = (num // 10) % 10
last = num % 10
sum_digits = first + second + last
prod_digits = first * second * last
if 10 <= sum_digits <= 99:
    print("Сумма цифр - двузначное число")
else:
    print("Сумма цифр не двузначна")

if 100 <= prod_digits <= 999:
    print("Произведение цифр - трехзначное число")
else:
    print("Произведение цифр не трехзначно")

if prod_digits > a:
    print("Произведение цифр больше a")
elif prod_digits < a:
    print("Произведение цифр меньше a")
else:
    print("Произведение цифр равно a")

if sum_digits % 5 == 0:
    print("Сумма цифр кратна 5")
else:
    print("Сумма цифр не кратна 5")

if num % sum_digits == 0:
    print("Число делится на сумма своих цифр")
else:
    print("Число не делится на сумму своих цифр")