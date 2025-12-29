a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
print("Совершенные числа в диапазоне:")
for num in range(a, b + 1):
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    if sum_divisors == num:
        print(num)