a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
max_val = a if a > b else b
min_val = a if a < b else b
print(f"Максимальное значение: {max_val}")
print(f"Минимальное значение: {min_val}")