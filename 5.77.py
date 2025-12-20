for num in range(10, 100):
    if num % 2 == 1 and (num % 10 == 3 or num % 10 == 7):
        print(num, end=" ")