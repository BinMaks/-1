arr = [float(x) for x in input("Введите вещественные числа: ").split()]
k1 = float(input("k1: "))
k2 = float(input("k2: "))
arr = [x - k1 if x > 0 else x - k2 for x in arr]
print("Результат:", arr)



arr = [float(x) for x in input("Введите вещественные числа: ").split()]
for i in range(len(arr)):
    if i % 2 == 0:
        arr[i] -= 1
    else:
        arr[i] += 1
print("Результат:", arr)