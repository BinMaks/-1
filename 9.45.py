
def sum_digits_sq(num):
    s = 0
    while num:
        s += num % 10
        num //= 10
    return s * s
m, n = map(int, input("m и n: ").split())
for num in range(1, n):
    if sum_digits_sq(num) == m:
        print(num)