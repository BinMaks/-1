n = int(input("Количество пар: "))
pairs = []
for _ in range(n):
    a, b = map(float, input("Введите a и b: ").split())
    pairs.append((a, b))
max_avg = -1
max_idx = -1
for i, (a, b) in enumerate(pairs):
    avg = (a + b) / 2
    if avg >= max_avg:
        max_avg = avg
        max_idx = i + 1
print(f"а) Номер пары с макс. средним арифметическим: {max_idx}")
min_geo = float('inf')
min_idx = -1
for i, (a, b) in enumerate(pairs):
    geo = (a * b) ** 0.5
    if geo < min_geo:
        min_geo = geo
        min_idx = i + 1
print(f"б) Номер пары с мин. средним геометрическим: {min_idx}")