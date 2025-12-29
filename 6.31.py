n = int(input("Введите число: "))
odd_count = 0
while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        odd_count += 1
    n = n // 10
print("Количество нечетных цифр:", odd_count)