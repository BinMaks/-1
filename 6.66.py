def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))

print("Числа, у которых количество цифр равно количеству делителей:")
for num in range(a, b + 1):
    if count_digits(num) == count_divisors(num):
        print(num, end=" ")