
n = int(input("Введите n: "))
for i in range(1, n + 1):
    divisors = [j for j in range(1, i + 1) if i % j == 0]
    print(f"{i} {'+' * len(divisors)}")