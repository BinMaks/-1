a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
k = int(input("Введите k: "))
print(f"Числа, у которых произведение цифр равно {k}:")
for num in range(a, b + 1):
    product = 1
    temp = num
    while temp > 0:
        product *= temp % 10
        temp //= 10
    if product == k:
        print(num, end=" ")