a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
k = int(input("Введите k: "))
print(f"Числа, у которых сумма цифр делится на {k}:")
for num in range(a, b + 1):
    digit_sum = 0
    temp = num
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    if digit_sum % k == 0:
        print(num, end=" ")