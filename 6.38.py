n = int(input("Введите число: "))
power = 1
while power * 2 <= n:
    power *= 2
print("Максимальная степень двойки:", power)