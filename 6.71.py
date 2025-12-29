def digit_sum_and_product(n):
    s = 0
    p = 1
    while n > 0:
        digit = n % 10
        s += digit
        p *= digit
        n //= 10
    return s, p

a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))

print("Числа, у которых произведение равно сумме цифр:")
for num in range(a, b + 1):
    s, p = digit_sum_and_product(num)
    if s == p:
        print(num, end=" ")