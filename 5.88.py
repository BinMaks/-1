s = int(input("Введите s (0 < s < 27): "))
count = 0
for num in range(100, 1000):
    digits = [int(d) for d in str(num)]
    if sum(digits) == s:
        count += 1
print("Количество:", count)