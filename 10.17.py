import random

dominoes = [(i, j) for i in range(7) for j in range(i, 7)]
domino1 = random.choice(dominoes)
domino2 = random.choice(dominoes)
print(f"Первая кость: {domino1[0]}-{domino1[1]}")
print(f"Вторая кость: {domino2[0]}-{domino2[1]}")
def can_connect(domino1, domino2):
    return (domino1[0] == domino2[0] or
            domino1[0] == domino2[1] or
            domino1[1] == domino2[0] or
            domino1[1] == domino2[1])
if can_connect(domino1, domino2):
    print("Кости можно соединить")
else:
    print("Кости нельзя соединить")
if can_connect(domino1, domino2):
    if domino1[0] in domino2:
        print(f"Соединение по точке {domino1[0]}")
    elif domino1[1] in domino2:
        print(f"Соединение по точке {domino1[1]}")