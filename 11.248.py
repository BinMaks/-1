a = list(map(int, input("Массив a: ").split()))
b = [a[i] * 2 if a[i] % 2 == 0 else a[i] for i in range(len(a))]
print("Массив b:", b)