for i in range(20, 36):
    print(i)

a = int(input("Введите a (<= 50): "))
for i in range(a, 51):
    print(i ** 2)

b = int(input("введите b (>= 10): "))
for i in range(10, b+1):
    print(i ** 3)

a = int(input("Введите a: "))
b = int(input("Введите b (>=a): "))
for i in range(a, b+1):
    print(i)