for num in range(50, 71):
    div_sum = sum(i for i in range(1, num + 1) if num % i == 0)
    print(f"{num}: {div_sum}")