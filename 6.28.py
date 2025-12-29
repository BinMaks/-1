n = int(input("Введите число: "))
min_digit = 9
while n > 0:
    digit = n % 10
    if digit < min_digit:
        min_digit = digit
    n = n // 10
print("Минимальная цифра:", min_digit)