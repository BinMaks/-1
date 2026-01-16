a = list(map(int, input("Первый массив: ").split()))
b = list(map(int, input("Второй массив: ").split()))
c = [1 if (a[i] > 0 and b[i] > 0) or (a[i] < 0 and b[i] < 0) else 0 for i in range(len(a))]
print("Результат:", c)