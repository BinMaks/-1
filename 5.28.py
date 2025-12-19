product = 1
for i in range(7, 15):
    product *= i
print(f"Произведение: {product}")


a = int(input("Введите a (1 < a < 15): "))
product = 1
for i in range(a, 16):
    product *= i
print(f"Произведение: {product}")


b = int(input("Введите b (1 < b < 10): "))
product = 1
for i in range(1, b + 1):
    product *= i
print(f"Произведение: {product}")


a = int(input("Введите a: "))
b = int(input("Введите b (b > a): "))
product = 1
for i in range(a, b + 1):
    product *= i
print(f"Произведение: {product}")