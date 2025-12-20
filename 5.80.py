n = int(input("Введите n: "))
for num in range(10, 100):
    if num % n == 0 or str(n) in str(num):
        print(num, end=" ")