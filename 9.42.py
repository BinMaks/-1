
for num in range(100, 1000):
    a, b, c = num // 100, (num // 10) % 10, num % 10
    if a != b and a != c and b != c:
        print(num)