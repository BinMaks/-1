n = int(input("Введите n: "))
m = int(input("Введите m: "))
q = int(input("Введите q: "))
a = [int(input(f"a{i+1} = ")) for i in range(n)]
sum_a = sum(x for x in a if x <= m)
print("Сумма чисел ≤ m превышает q:", sum_a > q)