n = int(input("Введите n: "))
num = 1
while num * num <= n:
    num += 1
print("Первое число, квадрат которого больше", n, ":", num)