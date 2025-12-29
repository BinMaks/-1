def sum_of_divisors(n):
    sum_div = 0
    for i in range(1, n):
        if n % i == 0:
            sum_div += i
    return sum_div
a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
print("Дружественные числа в диапазоне:")
for i in range(a, b + 1):
    for j in range(i + 1, b + 1):
        if sum_of_divisors(i) == j and sum_of_divisors(j) == i:
            print(f"({i}, {j})")