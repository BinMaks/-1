a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
print("Числа с равным количеством четных и нечетных цифр:")
for num in range(a, b + 1):
    even_count = 0
    odd_count = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        temp //= 10
    if even_count == odd_count:
        print(num, end=" ")