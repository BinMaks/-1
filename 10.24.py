import random

def generate_coordinates():
    while True:
        a, b, c, d = random.randint(1, 8), random.randint(1, 8), random.randint(1, 8), random.randint(1, 8)
        if a != c and b != d:
            if abs(a - c) != abs(b - d):
                if abs(a - c) <= 1 and abs(b - d) <= 1:
                    if not (a == c or b == d or abs(a - c) == abs(b - d)):
                        return a, b, c, d
a, b, c, d = generate_coordinates()
print(f"Координаты: Ладья ({a}, {b}), другая точка ({c}, {d})")