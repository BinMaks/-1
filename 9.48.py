def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors
n = int(input("Введите число: "))
factors = prime_factors(n)
print("Простые множители (без повторов):", sorted(set(factors)))
print("Простые множители (с учётом кратности):", factors)