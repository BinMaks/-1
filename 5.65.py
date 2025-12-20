n = int(input("Введите натуральное число: "))
square = 0
current_odd = 1
for _ in range(n):
    square += current_odd
    current_odd += 2
print(f"Квадрат числа {n} равен {square}")