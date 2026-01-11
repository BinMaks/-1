
def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n
number = int(input("Введите число: "))
print("Цифровой корень:", digital_root(number))