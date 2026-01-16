scores = list(map(int, input("Введите очки команды (3, 1, 0): ").split()))
win_index = None
loss_index = None
for i, score in enumerate(scores):
    if score == 3 and win_index is None:
        win_index = i
    if score == 0 and loss_index is None:
        loss_index = i
if win_index is None:
    print("Выигрышей (3 очка) не было")
elif loss_index is None:
    print("Проигрышей (0 очков) не было")
elif win_index < loss_index:
    print("Первый выигрыш был раньше первого проигрыша")
else:
    print("Первый проигрыш был раньше первого выигрыша")