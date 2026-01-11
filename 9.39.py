
def from_base(digits, base):
    n = 0
    for digit in digits:
        n = n * base + digit
    return n

digits = list(map(int, input("Введите цифры числа: ").split()))
base = int(input("Введите основание системы счисления: "))
print(f"Десятичное значение: {from_base(digits, base)}")