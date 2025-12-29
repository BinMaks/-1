
def sum_of_divisors(n):
    total = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
target_sum = int(input("Введите сумму делителей: "))

print(f"Числа, у которых сумма делителей равна {target_sum}:")
for num in range(a, b + 1):
    if sum_of_divisors(num) == target_sum:
        print(num, end=" ")