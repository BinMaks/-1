import random

def count_frequency(n):
    zeros = 0
    ones = 0
    for _ in range(n):
        result = random.randint(0, 1)
        if result == 0:
            zeros += 1
        else:
            ones += 1
    return zeros / n, ones / n