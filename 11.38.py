arr = [int(x) for x in input("Введите целые числа: ").split()]
arr = [x / 2 if x % 10 == 4 else x for x in arr]
print("Результат:", arr)


arr = [int(x) for x in input("Введите целые числа: ").split()]
arr = [x ** 2 if x % 2 == 0 else x * 2 for x in arr]
print("Результат:", arr)

arr = [int(x) for x in input("Введите целые числа: ").split()]
a = int(input("a: "))
b = int(input("b: "))
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr[i] += a
    if i % 2 == 0:
        arr[i] -= b
print("Результат:", arr)