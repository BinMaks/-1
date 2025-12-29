
n = int(input("Введите натуральное число: "))
product = 1
while n > 0:
    product *= n % 10
    n = n // 10
print("Произведение цифр:", product)