m = float(input("Введите m (0.52 <= m <= 33.7): "))
results = []
for x in range(1, 101):
    y = (x ** 2 + 100) / (x + 200)
    if y < m:
        results.append(y)
print("Числа последовательности, меньшие m:", results)