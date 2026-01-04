sequence = []
while True:
    num = int(input("Введите число (-1 для завершения): "))
    if num == -1:
        break
    sequence.append(num)

position = -1
for i, num in enumerate(sequence):
    if num % 7 == 0:
        position = i + 1
        break

if position != -1:
    print(f"Первое число, кратное 7, находится на позиции {position}")
else:
    print("Чисел, кратных 7, нет")