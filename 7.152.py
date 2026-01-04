a = [float(input(f"a[{i+1}]: ")) for i in range(15)]
n = float(input("Число n: "))

closest_idx = 0
min_diff = abs(a[0] - n)

for i in range(1, 15):
    diff = abs(a[i] - n)
    if diff < min_diff:
        min_diff = diff
        closest_idx = i

print(f"Ближайший элемент: a[{closest_idx+1}] = {a[closest_idx]}")