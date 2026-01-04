
seq = []
while True:
    num = int(input())
    if num == 100:
        break
    seq.append(num)

first_666_idx = -1
for i, num in enumerate(seq):
    if num == 666:
        first_666_idx = i
        break

if first_666_idx != -1:
    print("Число 666 есть. Первое на позиции:", first_666_idx + 1)
else:
    print("Числа 666 нет.")