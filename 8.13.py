a = float(input("Введите a: "))
sum_val = 0
n = 1
while sum_val <= a:
    sum_val += 1 / n
    n += 1
print(f"Наименьшее n: {n - 1}") 