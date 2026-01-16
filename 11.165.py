arr = list(map(int, input("Введите элементы: ").split()))
unique = []
for x in arr:
    if x not in unique:
        unique.append(x)
print(unique)

