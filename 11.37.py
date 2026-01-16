arr = [float(x) for x in input("Введите вещественные числа: ").split()]
a1 = float(input("a1: "))
b = float(input("b: "))
arr = [x + a1 if x < 0 else x - b if x == 0 else x for x in arr]
print("Результат:", arr)

arr = [float(x) for x in input("Введите вещественные числа: ").split()]
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
arr = [x - a if x > 0 else x - b if x < 0 else x + c for x in arr]
print("Результат:", arr)