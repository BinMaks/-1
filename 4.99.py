a, b = map(float, input("Введите два числа: ").split())
max_val = a
if b > a: max_val = b
print(f"Наибольшее число: {max_val}")

a, b = map(float, input("Введите два числа: ").split())
max_val = a if a > b else b
print(f"Наибольшая число: {max_val}")
