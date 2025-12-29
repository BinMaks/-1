a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
print("Числа, где сумма цифр делится на их количество:")
for num in range(a, b + 1):
    digit_sum = 0
    digit_count = 0
    temp = num
    while temp > 0:
        digit_sum += temp % 10
        digit_count += 1
        temp //= 10
    if digit_sum % digit_count == 0:
        print(num, end=" ")