a = float(input("Введите a: "))
n = int(input("Введите n: "))
current = a
for i in range(1, n + 1):
    print(f"a^{i} = {current}")
    current *= a