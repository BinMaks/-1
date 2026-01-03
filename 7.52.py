b = [int(input(f"b{i+1} = ")) for i in range(14)]
sum_gt_20 = sum(x for x in b if x > 20)
sum_lt_50 = sum(x for x in b if x < 50)
print("а) Сумма чисел > 20 превышает 100:", sum_gt_20 > 100)
print("б) Сумма чисел < 50 четная:", sum_lt_50 % 2 == 0)