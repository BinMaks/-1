factorial = int(input("Введите факториал: "))
n = 1
current_factorial = 1
while current_factorial < factorial:
    n += 1
    current_factorial *= n
if current_factorial == factorial:
    print("Число:", n)
else:
    print("Введенное число не является факториалом")