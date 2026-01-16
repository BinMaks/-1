arr = [int(x) for x in input("Введите целые числа: ").split()]
arr = [0 if x % 10 == 0 else x for x in arr]
print("Результат:", arr)

arr = [int(x) for x in input("Введите целые числа: ").split()]
arr = [0 if x % 10 == 5 else x for x in arr]
print("Результат:", arr)

arr = [int(x) for x in input("Введите целые числа: ").split()]
arr = [0 if x % 3 == 0 or x % 5 == 0 else x for x in arr]
print("Результат:", arr)

arr = [int(x) for x in input("Введите целые числа: ").split()]
arr = [0 if x % 7 == 0 else x + 1 for x in arr]
print("Результат:", arr)


arr = [int(x) for x in input("Введите целые числа: ").split()]
for i in range(len(arr)):
    if i % 2 == 0:
        arr[i] = 0
    else:
        arr[i] += 2
print("Результат:", arr)

arr = [int(x) for x in input("Введите целые числа: ").split()]
avg = sum(arr) / len(arr)
arr = [0 if x < avg else x for x in arr]
print("Результат:", arr)

arr = [int(x) for x in input("Введите целые числа: ").split()]
max_val = max(arr)
threshold = max_val - 10
arr = [0 if x > threshold else x for x in arr]
print("Результат:", arr)