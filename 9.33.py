
def sum_of_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

friendly_pairs = []
for a in range(2, 50000):
    b = sum_of_divisors(a)
    if b > a and sum_of_divisors(b) == a:
        friendly_pairs.append((a, b))
print(friendly_pairs)