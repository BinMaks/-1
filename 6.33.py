
n = int(input("Введите число: "))
sum_divisors = 0
for i in range(1, n):
    if n % i == 0:
        sum_divisors += i
if sum_divisors == n:
    print("Число совершенное")
else:
    print("Число не совершенное")