a = [5, -3, 8, -1, 0, -7, 2, -4, 9, -2]
b = []
for num in a:
    if num < 0:
        b.append(num)
print("Отрицательные числа:", b)