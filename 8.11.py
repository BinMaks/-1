
n = int(input("Введите n: "))
sum_val = 1
current_n = 2
while sum_val <= n:
    sum_val += 1 / current_n
    current_n += 1
print(f"Первое число, большее {n}: {sum_val}")