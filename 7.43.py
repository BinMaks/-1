
nums = [int(input(f"Число {i+1} = ")) for i in range(10)]
sum_nums = sum(x for x in nums if x % 10 == 0)
print("Сумма чисел, оканчивающихся на 0:", sum_nums)