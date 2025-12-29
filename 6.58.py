a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
k = int(input("Введите разность: "))
print(f"Числа с разностью max и min цифр {k}:")
for num in range(a, b + 1):
    digits = []
    temp = num
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10
    if max(digits) - min(digits) == k:
        print(num, end=" ")