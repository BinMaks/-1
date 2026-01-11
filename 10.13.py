import random

def roll_dice_twice():
    return [random.randint(1, 6) for _ in range(2)]
player1_rolls = roll_dice_twice()
player2_rolls = roll_dice_twice()
player1_sum = sum(player1_rolls)
player2_sum = sum(player2_rolls)
print(f"Игрок 1: {player1_rolls}, сумма: {player1_sum}")
print(f"Игрок 2: {player2_rolls}, сумма: {player2_sum}")
if player1_sum > player2_sum:
    print("Выиграл игрок 1!")
elif player2_sum > player1_sum:
    print("Выиграл игрок 2!")
else:
    print("Ничья!")