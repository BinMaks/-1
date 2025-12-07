num = int(input("Четырехзначное число: "))
a = int(input("Числа a: "))
first = num // 1000
second = (num // 100) % 10
third = (num // 10) % 10
last = num % 10
sum_first_two = first + second
sum_last_two = third + last
if sum_first_two == sum_last_two:
    print("Суммы равны ")
else:
    print("Суммы не равны")
sum_digits = first + second + third + last
if sum_digits % 3 == 0:
    print("Сумма цифр кратна 3")
else:
    print("Сумма цифр не кратна 3")

prod_digits = first * second * third * last
if prod_digits % 4 == 0:
    print("Произведение цифр кратно 4")
else:
    print("Произведение цифр не кратно 4")

if prod_digits % a == 0:
    print(f"произведение цифр кратно {a}")
else:
    print(f"Произведение цифр не кратно {a}")