n = int(input("Введите n: "))
m = int(input("Введите m: "))
p = int(input("Введите p: "))
c = [int(input(f"c{i+1} = ")) for i in range(n)]
sum_c = sum(x for x in c if x <= m)
print("Сумма чисел ≤ m кратна p:", sum_c % p == 0)