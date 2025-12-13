a2 = int(input("Десятки двузначного числа: "))
a1 = int(input("Единицы двузначного числа: "))
b = int(input("Однозначное число: "))
a = a2 * 10 + a1
diff = a - b
diff_tens = diff // 10
diff_units = diff % 10
print(f"Разность: {diff}")
print(f"Десятки разности: {diff_tens}")
print(f"Единицы разности: {diff_units}")