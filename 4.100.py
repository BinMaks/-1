a, b = map(float, input("Введите два числа: ").split())
max_val = a
min_val = a
if b > a: max_val = b
if b < a: min_val = b
print(f"Наибольшая: {max_val}, наименьшее: {min_val}")

a, b = map(float, input("Введите два числа: ").split())
max_val = a if a > b else b
min_val = a if a < b else b
print(f"наибольшее: {max_val}, наименьшее: {min_val}")

