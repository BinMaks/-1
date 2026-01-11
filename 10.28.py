import random

N = 1000000
count = 0
for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        count += 1
pi_estimate = 4 * (count / N)
print(f"π ≈ {pi_estimate}")