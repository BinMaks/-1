a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
target_sum = int(input("Введите сумму цифр: "))
print(f"Числа с суммой цифр {target_sum}:")
for num in range(a, b + 1):
    digit_sum = 0
    temp = num
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    if digit_sum == target_sum:
        print(num, end=" ")