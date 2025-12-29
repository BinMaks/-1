a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
print("Числа, где произведение = сумме цифр:")
for num in range(a, b + 1):
    digit_sum = 0
    digit_prod = 1
    temp = num
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        digit_prod *= digit
        temp //= 10
    if digit_prod == digit_sum:
        print(num, end=" ")