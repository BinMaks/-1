def prime_divisors(n):
    divisors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            divisors.add(d)
            n //= d
        d += 1
    if n > 1:
        divisors.add(n)
    return sorted(divisors)
n = int(input("Введите число: "))
print("Простые делители:", prime_divisors(n))