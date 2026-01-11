def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def divisors(n):
    result = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
    return sorted(result)
p, q = map(int, input("Введите p и q: ").split())
divs = divisors(q)
coprime_divs = [d for d in divs if gcd(d, p) == 1]
print("Делители", q, "взаимно простые с", p, ":", coprime_divs)