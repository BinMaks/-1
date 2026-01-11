import random

def white_pawn():
    a = random.randint(1, 8)
    b = random.randint(1, 6)
    d = b + 1
    c = random.choice([a, a - 1, a + 1])
    return a, b, c, d
def black_pawn():
    a = random.randint(1, 8)
    b = random.randint(2, 8)
    d = b - 1
    c = random.choice([a, a - 1, a + 1])
    return a, b, c, d
def knight():
    while True:
        a, b = random.randint(1, 8), random.randint(1, 8)
        da, db = random.choice([(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)])
        c, d = a + da, b + db
        if 1 <= c <= 8 and 1 <= d <= 8:
            return a, b, c, d
print("Белая пешка:", white_pawn())
print("Чёрная пешка:", black_pawn())
print("Конь угрожает полю:", knight())