import random

suits = ["пики", "трефы", "бубны", "червы"]
ranks = ["6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
def get_card():
    return (random.choice(suits), random.choice(ranks))
player1_card = get_card()
player2_card = get_card()
print(f"Игрок 1: {player1_card[1]} {player1_card[0]}")
print(f"Игрок 2: {player2_card[1]} {player2_card[0]}")
suit_priority = {suit: i for i, suit in enumerate(suits)}
rank_priority = {rank: i for i, rank in enumerate(ranks)}
p1_priority = suit_priority[player1_card[0]] * 10 + rank_priority[player1_card[1]]
p2_priority = suit_priority[player2_card[0]] * 10 + rank_priority[player2_card[1]]
if p1_priority > p2_priority:
    print("Выиграет игрок 1!")
elif p2_priority > p1_priority:
    print("Выиграет игрок 2!")
else:
    print("Ничья!")