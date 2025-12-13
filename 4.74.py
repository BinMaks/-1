a2 = int(input("Введите десятки первого числа: "))
a1 = int(input("Введите единицы первого числа: "))
b2 = int(input("Введите десятки второго числа: "))
b1 = int(input("Введите единицы второго числа: "))
diff_units = a1 - b1
diff_tens = a2 - b2
if diff_units < 0:
    diff_units += 10
    diff_tens -= 1
print(f"Цифры разности: десятки = {diff_tens}, единицы = {diff_units}")