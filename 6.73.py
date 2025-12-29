def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count
n = int(input("Введите число: "))
print("Количество делителей:", count_divisors(n))