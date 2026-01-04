numbers = [int(input(f"Число {i+1}: ")) for i in range(12)]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 != 0]
avg_even = sum(even_nums) / len(even_nums) if even_nums else 0
avg_odd = sum(odd_nums) / len(odd_nums) if odd_nums else 0
print(f"Среднее арифметическое четных чисел: {avg_even}")
print(f"Среднее арифметическое нечетных чисел: {avg_odd}")