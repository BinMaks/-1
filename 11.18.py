arr = []
num = 300
while len(arr) < 20:
    if num % 13 == 0 or num % 17 == 0:
        arr.append(num)
    num += 1
print(arr)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

arr = []
num = 2
while len(arr) < 30:
    if is_prime(num):
        arr.append(num)
    num += 1
print(arr)