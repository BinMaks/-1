n = int(input("Введите натуральное число: "))
sum_digits = 0
while n > 0:
    sum_digits += n % 10
    n = n // 10
print("Сумма цифр:", sum_digits)