number = int(input("Введите натуральное число: "))
count = 0
while number > 0:
    number //= 10
    count += 1
print("Количество цифр:", count)