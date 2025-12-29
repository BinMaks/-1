a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
print("Числа с цифрами в порядке возрастания:")
for num in range(a, b + 1):
    prev_digit = 10
    temp = num
    while temp > 0:
        digit = temp % 10
        if digit >= prev_digit:
            break
        prev_digit = digit
        temp //= 10
    else:
        print(num, end=" ")