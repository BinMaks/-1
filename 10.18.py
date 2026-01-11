import random

a = random.randint(1, 9)
b = random.randint(1, 9)
result = a * b
answer = int(input(f"Чему равно произведение {a} × {b}? "))
if answer == result:
    print("Правильно!")
else:
    print(f"Неправильно. Правильный ответ: {result}")



import random

correct = 0
incorrect = 0

for _ in range(20):
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    result = a * b
    answer = int(input(f"Чему равно произведение {a} × {b}? "))
    if answer == result:
        print("Правильно!")
        correct += 1
    else:
        print(f"Неправильно. Правильный ответ: {result}")
        incorrect += 1
print(f"Правильных ответов: {correct}")
print(f"Неправильных ответов: {incorrect}")


import random

while True:
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    result = a * b
    answer = int(input(f"Чему равно произведение {a} × {b}? (Для выхода введите 0) "))
    if answer == 0:
        break
    elif answer == result:
        print("Правильно!")
    else:
        print(f"Неправильно. Правильный ответ: {result}")