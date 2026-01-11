import random

dominoes = [(i, j) for i in range(7) for j in range(i, 7)]  # Уникальные кости
chosen_domino = random.choice(dominoes)
print(f"Выбрана кость {chosen_domino[0]}-{chosen_domino[1]}")