for num in range(start, end + 1):
    div_sum = sum(i for i in range(1, num + 1) if num % i == 0)
    if div_sum == target or div_sum % 10 == 0:
        print(num)