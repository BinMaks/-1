arr = [float(x) for x in input("Введите вещественные числа: ").split()]
m1 = float(input("m1: "))
m2 = float(input("m2: "))
arr = [x + m1 if x < 0 else x + m2 for x in arr]
print("Результат:", arr)

arr = [float(x) for x in input("Введите вещественные числа: ").split()]
for i in range(len(arr)):
    if i % 2 == 0:
        arr[i] *= 2
    else:
        arr[i] -= 1
print("Результат:", arr)