n = int(input("Введите n: "))
m = [int(input(f"m{i+1} = ")) for i in range(n)]
sum_lt_25_5 = sum(x for x in m if x < 25.5)
sum_le_20 = sum(x for x in m if x <= 20)
print("а) Сумма mᵢ < 25.5 ≤ 50:", sum_lt_25_5 <= 50)
print("б) Сумма mᵢ ≤ 20 кратна 3:", sum_le_20 % 3 == 0)