import random

a, b, c, d, e, f = [random.randint(1, 8) for _ in range(6)]
print(f"Белая ладья: ({a}, {b}), чёрная ладья: ({c}, {d}), цель: ({e}, {f})")
white_can_move = (a == e) or (b == f)
black_threatens = (c == e) or (d == f)
if white_can_move and not black_threatens:
    print("Белая ладья может пойти на (e, f) без угрозы.")
else:
    print("Белая ладья не может пойти на (e, f) без угрозы или не доходит.")