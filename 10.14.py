import random

k = int(input("Сколько кубиков бросать каждому? "))
def roll_dice_k_times(k):
    return sum(random.randint(1, 6) for _ in range(k))
player1_score = roll_dice_k_times(k)
player2_score = roll_dice_k_times(k)
player3_score = roll_dice_k_times(k)
print(f"Игрок 1: {player1_score}")
print(f"Игрок 2: {player2_score}")
print(f"Игрок 3: {player3_score}")
max_score = max(player1_score, player2_score, player3_score)
if player1_score == max_score:
    print("Выиграл игрок 1!")
elif player2_score == max_score:
    print("Выиграл игрок 2!")
elif player3_score == max_score:
    print("Выиграл игрок 3!")
else:
    print("Ничья!")