sequence = []
while True:
    num = int(input("Введите число (0 для завершения): "))
    if num == 0:
        break
    sequence.append(num)

position = -1
for i, num in enumerate(sequence):
    if num % 10 == 7:
        position = i + 1
        break

if position != -1:
    print(f"Первое число, оканчивающееся на 7, находится на позиции {position}")
else:
    print("Чисел, оканчивающихся на 7, нет")