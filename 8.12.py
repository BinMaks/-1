a = float(input("Введите a: "))
sum_val = 0
n = 1
results = []
while sum_val <= a:
    sum_val += 1 / n
    n += 1
while sum_val > a:
    results.append(n - 1)  
    sum_val -= 1 / (n - 1)
    if sum_val <= a:
        break
print("Значения n, удовлетворяющие условию:", results)