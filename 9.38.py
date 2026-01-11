
def to_base(n, base):
    digits = []
    while n > 0:
        digits.append(n % base)
        n //= base
    return digits[::-1]

n = int(input("Введите число: "))
base = int(input("Введите основание системы счисления: "))
print(f"Число в системе счисления {base}: {to_base(n, base)}")