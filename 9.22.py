
def count_divisors(num):
    return len([i for i in range(1, num + 1) if num % i == 0])

for num in range(start, end + 1):
    if count_divisors(num) == target_divisors:
        print(num)