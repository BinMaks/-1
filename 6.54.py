a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
target_prod = int(input("Введите произведение цифр: "))
print(f"Числа с произведением цифр {target_prod}:")
for num in range(a, b + 1):
    product = 1
    temp = num
    while temp > 0:
        product *= temp % 10
        temp //= 10
    if product == target_prod:
        print(num, end=" ")