n = int(input("Введите число: "))
even_count = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even_count += 1
    n = n // 10
print("Количество четных цифр:", even_count)