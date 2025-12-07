num = int(input("Двузначное число: "))
sum_digits = num // 10 + num % 10
if sum_digits % 3 == 0:
    print("Сумма цифр кратна 3")
else:
    print("Сумма цифр не кратна 3")

if num % sum_digits == 0:
    print("Число делится на сумму своих цифр")
else:
    print("Число не делится на сумму своих цифр")