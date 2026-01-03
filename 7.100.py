
x = [float(input(f"x[{i}]: ")) for i in range(15)]
out_of_order = False
for i in range(1, len(x)):
    if x[i] < x[i-1]:
        print(f"Последовательность не упорядочена. Первое нарушение на позиции {i+1}")
        out_of_order = True
        break
if not out_of_order:
    print("Последовательность упорядочена по возрастанию")