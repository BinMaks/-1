
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
product = a * b
while b != 0:
    a, b = b, a % b
gcd = a
lcm = product // gcd
print("НОК:", lcm)