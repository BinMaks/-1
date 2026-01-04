
sequence = []
while True:
    num = int(input("Введите число (отрицательное для завершения): "))
    if num < 0:
        break
    sequence.append(num)

all_equal = len(sequence) == 0 or all(elem == sequence[0] for elem in sequence)
print("Все элементы равны между собой" if all_equal else "Элементы не равны между собой")