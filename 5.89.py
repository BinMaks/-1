
count = 0
for num in range(100, 1000):
    if num % 7 == 0:
        digits = [int(d) for d in str(num)]
        if sum(digits) % 7 == 0:
            count += 1
print("Количество:", count)