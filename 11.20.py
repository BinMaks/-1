import random

arr = []
for _ in range(20):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    answer = int(input(f"Чему равно произведение {a} на {b}? "))
    arr.append(answer == a * b)
print("Результаты:", arr)