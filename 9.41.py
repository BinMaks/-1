def sum_digits(num):
    s = 0
    while num:
        s += num % 10
        num //= 10
    return s
n = int(input("Сумма цифр (n <= 27): "))
for num in range(100, 1000):
    if sum_digits(num) == n:
        print(num)