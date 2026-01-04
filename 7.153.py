numbers = [int(input(f"Число {i+1}: ")) for i in range(14)]
even_numbers = [num for num in numbers if num % 2 == 0]

if even_numbers:
    print(f"Максимальное четное число: {max(even_numbers)}")
else:
    print("Четных чисел нет")