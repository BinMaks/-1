arr = [float(x) for x in input("Введите вещественные числа: ").split()]
k1 = float(input("k1: "))
n = float(input("n: "))
arr = [x - k1 if x > 0 else x - n if x < 0 else x for x in arr]
print("Результат:", arr)

arr = [float(x) for x in input("Введите вещественные числа: ").split()]
a = float(input("a: "))
b = float(input("b: "))
n = float(input("n: "))
arr = [x + n if x == 0 else x - a if x > 0 else x + b for x in arr]
print("Результат:", arr)