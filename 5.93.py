n = int(input("Введите натуральное число: "))
divisors_sum = 0
for i in range(1, n):
    if n % i == 0:
        divisors_sum += i
if divisors_sum == n:
    print("Число совершенное")
else:
    print("Число не совершенное")