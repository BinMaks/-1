def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def count_prime_divisors(n):
    count = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and is_prime(i):
            count += 1
            while n % i == 0:
                n //= i
    if n > 1 and is_prime(n):
        count += 1
    return count

a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))

print("Числа, у которых сумма цифр равна количеству простых делителей:")
for num in range(a, b + 1):
    if digit_sum(num) == count_prime_divisors(num):
        print(num, end=" ")