def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def has_increasing_prime_digits(n):
    prev_digit = -1
    while n > 0:
        digit = n % 10
        if not is_prime(digit) or digit <= prev_digit:
            return False
        prev_digit = digit
        n = n // 10
    return True

a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))

print("Числа с возрастающей последовательностью простых цифр:")
for num in range(a, b + 1):
    if has_increasing_prime_digits(num):
        print(num, end=" ")