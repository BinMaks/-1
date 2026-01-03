
n = int(input("Введите n: "))
x = int(input("Введите x: "))
a = [int(input(f"a[{i}]: ")) for i in range(n)]
count_negative = sum(1 for ai in a if ai < 0)
print("Количество отрицательных чисел превышает x" if count_negative > x else "Количество отрицательных чисел не превышает x")