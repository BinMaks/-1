def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
target_divisors = int(input("Введите количество делителей: "))

print(f"Числа с {target_divisors} делителями:")
for num in range(a, b + 1):
    if count_divisors(num) == target_divisors:
        print(num, end=" ")