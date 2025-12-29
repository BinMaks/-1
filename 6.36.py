
n = int(input("Введите число: "))
max_divisor = 1
for i in range(2, n):
    if n % i == 0:
        max_divisor = i
print("Наибольший делитель:", max_divisor)