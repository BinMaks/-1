
import random

suits = ["пики", "трефы", "бубны", "червы"]
ranks = ["6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
trump_suit = random.choice(suits)
print(f"Козырная масть: {trump_suit}")
chosen_suit = random.choice(suits)
chosen_rank = random.choice(ranks)
print(f"Выбрана карта: {chosen_rank} {chosen_suit}")
if chosen_suit == trump_suit:
    print("Эта карта козырная!")
else:
    print("Эта карта не козырная.")