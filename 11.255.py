a = list(map(int, input("Первый массив: ").split()))
b = list(map(int, input("Второй массив: ").split()))
c = [a[i] + b[i] for i in range(len(a))]
print("Сумма (а):", c)
d = [a[i] * b[i] for i in range(len(a))]
print("Произведение (б):", d)
e = [max(a[i], b[i]) for i in range(len(a))]
print("Максимум (в):", e)