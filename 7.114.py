d = [int(input(f"d[{i+1}] = ")) for i in range(14)]
even_nums = [num for num in d if num % 2 == 0]
if even_nums:
    average = sum(even_nums) / len(even_nums)
    print(f"Среднее арифметическое четных чисел: {average}")
else:
    print("Четных чисел нет")