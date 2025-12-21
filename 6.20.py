num = int(input("Введите натуральное число: "))
digits = [int(d) for d in str(num)]
sum_digits = sum(digits)
count_digits = len(digits)
product_digits = 1
for d in digits:
    product_digits *= d
print("Сумма цифр:", sum_digits)
print("Количество цифр:", count_digits)
print("Произведение цифр:", product_digits)