
sequence = [int(input(f"Число {i+1}: ")) for i in range(30)]
unique_numbers = set(sequence)
print(f"Количество различных чисел: {len(unique_numbers)}")