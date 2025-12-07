num = int(input("Трехзначное число" ))
first = num // 100
second = (num // 10) % 10
last = num % 10
if first == second == last:
    print("Все цифры одинаковые")
else:
    print("Цифры не одинаковые ")
if first == second or first == last or second == last:
    print("Есть одинаковые цифры")
else:
    print("Нет одинаковых цифр")