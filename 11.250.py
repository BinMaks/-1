a = list(map(int, input("Массив a: ").split()))
b = [a[i] if i % 2 == 1 else None for i in range(len(a))]
print("Вариант а):", b)
c = [a[i] for i in range(len(a)) if i % 2 == 1]
print("Вариант б):", c)