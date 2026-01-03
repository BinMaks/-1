n = int(input("Введите n: "))
p = float(input("Введите p: "))
b = [float(input(f"b{i+1} = ")) for i in range(n)]
sum_b = sum(x for x in b if x > p)
print("Сумма чисел > p:", sum_b)