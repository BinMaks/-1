p = list(map(int, input("Массив p: ").split()))
q = [-p[i] if 3 <= i <= 10 else p[i] * i for i in range(len(p))]
print("Массив q:", q)