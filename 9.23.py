
a, b, k = map(int, input("Введите a, b, k: ").split())
for num in range(a, b + 1):
    if len([i for i in range(1, num + 1) if num % i == 0]) == k:
        print(num)