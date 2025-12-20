n = int(input("Введите натуральное число: "))
divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
print("а) Делители числа:", divisors)
sum_divisors = sum(divisors)
print("б) Сумма делителей:", sum_divisors)
sum_even_divisors = sum(d for d in divisors if d % 2 == 0)
print("в) Сумма четных делителей:", sum_even_divisors)
count_divisors = len(divisors)
print("г) Количество делителей:", count_divisors)
count_odd_divisors = sum(1 for d in divisors if d % 2 == 1)
print("д) Количество нечетных делителей:", count_odd_divisors)
print("е) Количество делителей:", count_divisors)
print("   Количество четных делителей:", count_even_divisors // min(divisors) if divisors else 0)
d = int(input("Введите d: "))
count_greater_d = sum(1 for d_val in divisors if d_val > d)
print("ж) Количество делителей, больших", d, ":", count_greater_d)