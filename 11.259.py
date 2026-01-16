a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
k = int(input("Введите индекс k: "))
b = []
for i in range(len(a)):
    if i != k:
        b.append(a[i])
print("Новый массив:", b)