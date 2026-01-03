numbers = []
while True:
    num = float(input("Число (окончание ввода — 10000): "))
    if num == 10000:
        break
    numbers.append(num)

out_of_order = False
for i in range(1, len(numbers)):
    if numbers[i] < numbers[i-1]:
        print(f"Последовательность не упорядочена. Первое нарушение на позиции {i+1}")
        out_of_order = True
        break
if not out_of_order:
    print("Последовательность упорядочена по возрастанию")