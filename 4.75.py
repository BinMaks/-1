a3 = int(input("Введите сотни трехзначного числа: "))
a2 = int(input("Введите десятки трехзначного числа: "))
a1 = int(input("Введите единицы трехзначного числа: "))
b2 = int(input("Введите десятки двузначного числа: "))
b1 = int(input("Введите единицы двузначного числа: "))
sum_units = a1 + b1
sum_tens = a2 + b2 + (sum_units // 10)
sum_hundreds = a3 + (sum_tens // 10)
sum_units = sum_units % 10
sum_tens = sum_tens % 10
print(f"Цифры суммы: сотни = {sum_hundreds}, десятки = {sum_tens}, единицы = {sum_units}")