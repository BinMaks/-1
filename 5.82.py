for num in range(10, 100):
    tens, units = num // 10, num % 10
    if (tens ** 2 + units ** 2) % 13 == 0:
        print(num, end=" ")


for num in range(10, 100):
    tens, units = num // 10, num % 10
    digit_sum = tens + units
    if num == digit_sum + digit_sum ** 2:
        print(num, end=" ")