
n = int(input("Введите n: "))
p = float(input("Введите p: "))
d = [float(input(f"d{i+1} = ")) for i in range(n)]
sum_gt_20_5 = sum(x for x in d if x > 20.5)
print("Сумма dᵢ > 20.5 меньше p:", sum_gt_20_5 < p)