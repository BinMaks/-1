def is_prime_digit(d):
    return d in {2, 3, 5, 7}

a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))

print("Числа, у которых все цифры простые:")
for num in range(a, b + 1):
    temp = num
    while temp > 0:
        digit = temp % 10
        if not is_prime_digit(digit):
            break
        temp //= 10
    else:
        print(num, end=" ")