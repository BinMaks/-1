
m = list(map(int, input("Массив m: ").split()))
n = [m[i] / 3 if m[i] >= 0 else m[i] ** 2 for i in range(len(m))]
print("Массив n:", n)