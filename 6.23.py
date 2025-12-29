n = int(input("Введите натуральное число: "))
count = 0
while n > 0:
    n = n // 10
    count += 1
print("Количество цифр:", count)