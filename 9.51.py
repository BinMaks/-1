def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n, p = map(int, input("Введите n и p: ").split())
coprimes = []
for i in range(1, n):
    if gcd(i, p) == 1:
        coprimes.append(i)
print("Числа, взаимно простые с", p, "и меньшие", n, ":", coprimes)