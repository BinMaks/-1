
a, b = map(int, input("Введите a, b: ").split())
max_sum = 0
max_num = a
for num in range(a, b + 1):
    div_sum = sum(i for i in range(1, num + 1) if num % i == 0)
    if div_sum > max_sum:
        max_sum = div_sum
        max_num = num
print(f"Число с макс. суммой делителей: {max_num} (сумма: {max_sum})")