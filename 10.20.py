import random

suits = ["пики", "трефы", "бубны", "червы"]
ranks = ["6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
chosen_suit = random.choice(suits)
chosen_rank = random.choice(ranks)
print(f"Выбрана {chosen_rank} {chosen_suit}")