n = int(input("Введите n: "))
if n <= 0:
    print("n должно быть положительным!")
else:
    a, b = 1, 1
    fib_sum = a if n == 1 else a + b
    for _ in range(2, n):
        a, b = b, a + b
        fib_sum += b
    if fib_sum % 2 == 0:
        print("Сумма четная")
    else:
        print("Сумма нечетная")