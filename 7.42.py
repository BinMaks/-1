d = [int(input(f"d{i+1} = ")) for i in range(10)]
sum_d = sum(x for x in d if x % 2 == 0)
print("Сумма чётных чисел:", sum_d)