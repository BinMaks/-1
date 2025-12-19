
n = int(input("Введите n: "))
sum_squares = sum(i**2 for i in range(1, n + 1))
print(f"Сумма квадратов: {sum_squares}")