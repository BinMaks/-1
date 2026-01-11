def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
fractions = []
for denominator in range(2, 8):
    for numerator in range(1, denominator):
        if gcd(numerator, denominator) == 1:
            fractions.append((numerator, denominator))
print("Простые несократимые дроби:", fractions)