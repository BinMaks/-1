a, b = map(int, input("Координаты белой фигуры (a b): ").split())
c, d = map(int, input("Координаты чёрной фигуры (c d): ").split())
e, f = map(int, input("Целевое поле для хода (e f): ").split())
white_fig = input("Тип белой фигуры (ладья, ферзь, конь, слон, король): ").lower()
black_fig = input("Тип чёрной фигуры (ладья, ферзь, конь, слон, король): ").lower()
def threat_rook(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2
def threat_queen(x1, y1, x2, y2):
    return threat_rook(x1, y1, x2, y2) or abs(x1 - x2) == abs(y1 - y2)
def threat_knight(x1, y1, x2, y2):
    return (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2)
def threat_bishop(x1, y1, x2, y2):
    return abs(x1 - x2) == abs(y1 - y2)
def threat_king(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1
def can_move(fig, start_x, start_y, target_x, target_y):
    if fig == "ладья":
        return threat_rook(start_x, start_y, target_x, target_y)
    elif fig == "ферзь":
        return threat_queen(start_x, start_y, target_x, target_y)
    elif fig == "конь":
        return threat_knight(start_x, start_y, target_x, target_y)
    elif fig == "слон":
        return threat_bishop(start_x, start_y, target_x, target_y)
    elif fig == "король":
        return threat_king(start_x, start_y, target_x, target_y)
    else:
        return False
def is_threatened(fig, fig_x, fig_y, target_x, target_y):
    if fig == "ладья":
        return threat_rook(fig_x, fig_y, target_x, target_y)
    elif fig == "ферзь":
        return threat_queen(fig_x, fig_y, target_x, target_y)
    elif fig == "конь":
        return threat_knight(fig_x, fig_y, target_x, target_y)
    elif fig == "слон":
        return threat_bishop(fig_x, fig_y, target_x, target_y)
    elif fig == "король":
        return threat_king(fig_x, fig_y, target_x, target_y)
    else:
        return False
can_white_move = can_move(white_fig, a, b, e, f)
is_under_threat = is_threatened(black_fig, c, d, e, f)
if can_white_move and not is_under_threat:
    print("Белая фигура может пойти на поле ({}, {}) без угрозы.".format(e, f))
elif can_white_move and is_under_threat:
    print("Белая фигура может дойти до поля ({}, {}), но попадёт под удар чёрной фигуры.".format(e, f))
else:
    print("Белая фигура не может дойти до поля ({}, {}).".format(e, f))