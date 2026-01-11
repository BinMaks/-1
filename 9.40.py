
def is_perfect(n):
    sum_div = sum(i for i in range(1, n) if n % i == 0)
    return sum_div == n

n = int(input("Введите число: "))
if is_perfect(n):
    print("Число совершенное")
else:
    print("Число не совершенное")