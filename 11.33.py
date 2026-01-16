import math
arr = [float(x) for x in input("Введите вещественные числа: ").split()]
arr = [math.sqrt(x) if x > 10 else x for x in arr]
print("Результат:", arr)


arr = [float(x) for x in input("Введите вещественные числа: ").split()]
for i in range(0, len(arr), 2):
    arr[i] = abs(arr[i])
print("Результат:", arr)