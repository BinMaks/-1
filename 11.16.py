a = float(input("Первый член a: "))
d = float(input("Разность d: "))
arr = [a + i * d for i in range(10)]
print(arr)


a = float(input("Первый член a: "))
z = float(input("Знаменатель z: "))
arr = [a * (z ** i) for i in range(20)]
print(arr)