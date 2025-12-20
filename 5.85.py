a = int(input("Введите a: "))
b = int(input("Введите b: "))
total = 0
for num in range(a, b + 1):
    if num % 4 == 0:
        total += num
print("Сумма:", total)