
a = list(map(int, input("Массив a: ").split()))
pos = [a[i] if a[i] > 0 else None for i in range(len(a))]
neg = [a[i] if a[i] <= 0 else None for i in range(len(a))]
print("Положительные (а):", pos)
print("Остальные (а):", neg)
pos_b = [a[i] for i in range(len(a)) if a[i] > 0]
neg_b = [a[i] for i in range(len(a)) if a[i] <= 0]
print("Положительные (б):", pos_b)
print("Остальные (б):", neg_b)