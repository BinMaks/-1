n = int(input("Введите n (1 < n < 10): "))
total_sum = 1.0  
for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    total_sum += 1 / factorial
print(f"Сумма ряда: {total_sum:.6f}")