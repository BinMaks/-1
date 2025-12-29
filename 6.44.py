
n = int(input("Введите число: "))
power = 1
while power * 3 <= n:
    power *= 3
print("Максимальная степень тройки:", power)