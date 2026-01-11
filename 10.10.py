import random

print("Чет (введите 2) или нечет (введите 1)?")
user_choice = int(input())
computer_choice = random.choice([1, 2])
print(f"Компьютер выбрал: {computer_choice}")
if user_choice == computer_choice:
    print("Вы угадали!")
else:
    print("Не угадали.")

import random

n = int(input("Сколько раз играть? "))
user_score = 0
computer_score = 0

for _ in range(n):
    print("Чет (введите 2) или нечет (введите 1)?")
    user_choice = int(input())
    computer_choice = random.choice([1, 2])
    print(f"Компьютер выбрал: {computer_choice}")
    if user_choice == computer_choice:
        user_score += 1
        print("Вы угадали!")
    else:
        computer_score += 1
        print("Не угадали.")
if user_score > computer_score:
    print(f"Счёт {user_score}:{computer_score} в вашу пользу. Вы выиграли!")
elif computer_score > user_score:
    print(f"Счёт {user_score}:{computer_score} в пользу компьютера. Вы проиграли!")
else:
    print(f"Счёт {user_score}:{computer_score}. Ничья!")



import random

correct = 0
incorrect = 0

while True:
    print("Чет (введите 2) или нечет (введите 1)?")
    user_choice = int(input())
    computer_choice = random.choice([1, 2])
    print(f"Компьютер выбрал: {computer_choice}")
    if user_choice == computer_choice:
        correct += 1
        print("Вы угадали!")
    else:
        incorrect += 1
        print("Не угадали.")
    continue_game = input("Продолжить ещё раз? (Да/Нет) ")
    if continue_game.lower() == "нет":
        break
print(f"Верных ответов: {correct}, неверных ответов: {incorrect}")
