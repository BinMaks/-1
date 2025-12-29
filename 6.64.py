def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
print("Числа, у которых сумма цифр простая:")
for num in range(a, b + 1):
    if is_prime(digit_sum(num)):
        print(num, end=" ")