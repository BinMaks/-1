for num in range(100, 1000):
    div_sum = sum(i for i in range(1, num) if num % i == 0)
    if div_sum == num:
        print(f"Совершенное число: {num}")
        break