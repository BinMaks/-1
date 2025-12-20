count = 0
for num in range(100, 501):
    digits = [int(d) for d in str(num)]
    if sum(digits) == 15:
        count += 1
print("Количество:", count)