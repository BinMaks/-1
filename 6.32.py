n = int(input("Введите число: "))
original = n
sum_digits = 0
while n > 0:
    sum_digits += n % 10
    n = n // 10

if original % sum_digits == 0:
    print("Число делится на сумму своих цифр")
else:
    print("Число не делится на сумму своих цифр")