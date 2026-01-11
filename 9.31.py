
for num in range(2, 100000):
    div_sum = sum(i for i in range(1, num) if num % i == 0)
    if div_sum == num:
        print(num)