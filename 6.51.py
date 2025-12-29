n = int(input("Введите число: "))
k = int(input("Введите k: "))
count = 0
while n > 0:
    digit = n % 10
    if digit > k:
        count += 1
    n = n // 10
print("Количество цифр, больших", k, ":", count)