def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))

print("Числа, у которых сумма цифр - степень двойки:")
for num in range(a, b + 1):
    if is_power_of_two(digit_sum(num)):
        print(num, end=" ")