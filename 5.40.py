number = int(input("Введите 9-значное число: "))
sum_digits = 0
while number > 0:
    sum_digits += number % 10  
    number //= 10
print(f"Сумма цифр: {sum_digits}")