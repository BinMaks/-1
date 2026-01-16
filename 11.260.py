
a = [1, 13, 5, 13, 8, 13, 9, 13, 7, 13]
b = []
for num in a:
    if num != 13:
        b.append(num)
print("Массив без 13:", b)