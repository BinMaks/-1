sum_cubes = sum(i**3 for i in range(25, 41))
print(f"Сумма кубов: {sum_cubes}")



a = int(input("Введите a (0 < a < 50): "))
if 0 < a < 50:
    sum_squares = sum(i**2 for i in range(a, 51))
    print(f"Сумма квадратов: {sum_squares}")
else:
    print("Ошибка: a должно быть в диапазоне (0, 50)")



n = int(input("Введите n (1 < n < 100): "))
if 1 < n < 100:
    sum_squares = sum(i**2 for i in range(1, n + 1))
    print(f"Сумма квадратов: {sum_squares}")
else:
    print("Ошибка: n должно быть в диапазоне (1, 100)")


a = int(input("Введите a: "))
b = int(input("Введите b (b > a): "))
if b > a:
    sum_squares = sum(i**2 for i in range(a, b + 1))
    print(f"Сумма квадратов: {sum_squares}")
else:
    print("Ошибка: b должно быть больше a")