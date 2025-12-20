total_sum = 0
for i in range(1, 13):
    square = 0
    current_odd = 1
    for _ in range(i):
        square += current_odd
        current_odd += 2
    total_sum += square
print("Сумма квадратов от 1 до 12:", total_sum)