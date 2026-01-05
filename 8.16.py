
m = float(input("Введите m (0.5 < m < 1): "))
n = 1
results = []
while True:
    current = n / (n + 1)
    if current < m:
        results.append(current)
        n += 1
    else:
        break
print("Числа последовательности, меньшие m:", results)