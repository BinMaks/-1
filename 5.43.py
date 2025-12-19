n = int(input("Введите n: "))
a = 1
sequence = [a]
for k in range(1, n + 1):
    a = k * a + 1 / k
    sequence.append(a)
print("Последовательность:", sequence)