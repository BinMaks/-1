a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
print("Числа с различными цифрами:")
for num in range(a, b + 1):
    digits = set()
    temp = num
    while temp > 0:
        digit = temp % 10
        if digit in digits:
            break
        digits.add(digit)
        temp //= 10
    else:
        print(num, end=" ")