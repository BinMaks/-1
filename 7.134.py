sequence = []
while True:
    num = float(input("Введите число (0 для завершения): "))
    if num == 0:
        break
    sequence.append(num)

unique_numbers = set(sequence)
print(f"Количество различных чисел: {len(unique_numbers)}")