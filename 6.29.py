n = int(input("Введите число: "))
digit = int(input("Введите цифру для поиска: "))
found = False
while n > 0:
    if n % 10 == digit:
        found = True
        break
    n = n // 10
if found:
    print("Цифра найдена")
else:
    print("Цифра не найдена")