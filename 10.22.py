import random

suits = ["пики", "трефы", "бубны", "червы"]
ranks = ["6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
def get_card():
    return (random.choice(suits), random.choice(ranks))
def compare_cards(card1, card2):
    suit_priority = {suit: i for i, suit in enumerate(suits)}
    rank_priority = {rank: i for i, rank in enumerate(ranks)}
    p1_priority = suit_priority[card1[0]] * 10 + rank_priority[card1[1]]
    p2_priority = suit_priority[card2[0]] * 10 + rank_priority[card2[1]]
    if p1_priority > p2_priority:
        return "Игрок 1"
    elif p2_priority > p1_priority:
        return "Игрок 2"
    else:
        return "Ничья"
rounds = int(input("Количество раундов: "))
p1_wins = 0
p2_wins = 0
draws = 0
for _ in range(rounds):
    player1_card = get_card()
    player2_card = get_card()
    print(f"Игрок 1: {player1_card[1]} {player1_card[0]}, Игрок 2: {player2_card[1]} {player2_card[0]}")
    winner = compare_cards(player1_card, player2_card)
    print(winner)
    if winner == "Игрок 1":
        p1_wins += 1
    elif winner == "Игрок 2":
        p2_wins += 1
    else:
        draws += 1
print(f"Итог: Игрок 1 — {p1_wins}, Игрок 2 — {p2_wins}, Ничьи — {draws}")