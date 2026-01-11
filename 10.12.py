import random

player1_roll = random.randint(1, 6)
player2_roll = random.randint(1, 6)
print(f"Игрок 1: {player1_roll}")
print(f"Игрок 2: {player2_roll}")
if player1_roll > player2_roll:
    print("Выиграл игрок 1!")
elif player2_roll > player1_roll:
    print("Выиграл игрок 2!")
else:
    print("Ничья!")