a = list(map(int, input("Массив a: ").split()))
b = [a[i] ** 2 if i % 2 == 0 else 2 * a[i] for i in range(len(a))]
print("Массив b:", b)

