arr = [float(x) for x in input("Введите вещественные числа: ").split()]
arr = [abs(x) if x < 0 else x for x in arr]
print("Результат:", arr)

import math
arr = [float(x) for x in input("Введите вещественные числа: ").split()]
for i in range(1, len(arr), 2):
    arr[i] = math.sqrt(arr[i])
print("Результат:", arr)