def has_unique_descending_digits(n):
    prev_digit = 10
    seen_digits = set()
    while n > 0:
        digit = n % 10
        if digit >= prev_digit or digit in seen_digits:
            return False
        seen_digits.add(digit)
        prev_digit = digit
        n = n // 10
    return True

a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))

print("Числа с уникальными цифрами в порядке убывания:")
for num in range(a, b + 1):
    if has_unique_descending_digits(num):
        print(num, end=" ")