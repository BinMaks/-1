for num in range(100, 1000):
    square = num ** 2
    if square % 1000 == num:
        print(num, end=" ")


for num in range(100, 1000):
    if num % 7 == 0:
        digits = [int(d) for d in str(num)]
        if sum(digits) % 7 == 0:
            print(num, end=" ")