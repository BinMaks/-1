def digit_product(n):
    product = 1
    while n > 0:
        product *= n % 10
        n //= 10
    return product

def sum_of_divisors(n):
    total = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))

print("Числа, у которых произведение цифр равно сумме делителей:")
for num in range(a, b + 1):
    if digit_product(num) == sum_of_divisors(num):
        print(num, end=" ")