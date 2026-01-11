def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n = int(input("Введите число n: "))
coprimes = []
for i in range(1, n):
    if gcd(i, n) == 1:
        coprimes.append(i)
print("Числа, взаимно простые с", n, ":", coprimes)