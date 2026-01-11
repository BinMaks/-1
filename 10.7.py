import random

a = random.randint(0, 1)
b = random.randint(0, 2)
while a == b:
    b = random.randint(0, 2)
print(f"10.7.а) a = {a}, b = {b}")
a = random.randint(1, 2)
b = random.randint(0, 2)
c = random.randint(2, 3)
while a == b or a == c or b == c:
    a = random.randint(1, 2)
    b = random.randint(0, 2)
    c = random.randint(2, 3)
print(f"б) a = {a}, b = {b}, c = {c}")
numbers = [2] * 8
random.shuffle(numbers)
print("в) 15 чисел (7 двоек и 8 троек):", numbers)