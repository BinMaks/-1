number = int(input("Введите число: "))
n = int(input("Введите n: "))
product = 1
sum_digits = 0
for _ in range(n):
    digit = number % 10
    product *= digit
    sum_digits += digit
    number //= 10
print(f"Произведение: {product}")
print(f"Сумма: {sum_digits}")