n = int(input("Введите n (n > 3): "))
if n <= 2:
    print(1)
else:
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    print(f"n-й член: {b}")


n = int(input("Введите n (n > 3): "))
fib = [1, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print("Первые n членов:", fib)