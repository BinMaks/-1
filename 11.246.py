
m = list(map(int, input("Массив m: ").split()))
n = [i * m[i] if i % 2 == 1 else m[i] / i for i in range(len(m))]
print("Массив n:", n)