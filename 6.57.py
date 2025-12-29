a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
even_count = int(input("Введите количество четных цифр: "))
print(f"Числа с {even_count} четными цифрами:")
for num in range(a, b + 1):
    count = 0
    temp = num
    while temp > 0:
        if (temp % 10) % 2 == 0:
            count += 1
        temp //= 10
    if count == even_count:
        print(num, end=" ")