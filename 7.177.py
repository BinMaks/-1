
A = int(input("Введите A: "))
sequence = [8] * 4
sequence.append(A)
max_count = sequence.count(max(sequence))
print(f"Количество максимальных элементов: {max_count}")