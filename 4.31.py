num = int(input("Трехзначное число: "))
first = num // 100
second = (num // 10) % 10
last = num % 10
if first > last:
    print("Первая цифра больше последней")
elif first < last:
    print("Последняя цифра больше первой")
else:
    print("Первая и последняя цифры равны")

if first > second:
    print("Первая цифра больше второй")
elif first < second:
    print("Вторая цифра больше первой")
else:
    print("Первая и вторая цифры равны")

if second > last:
    print("Вторая цифра больше последней")
elif second < last:
    print("Последняя цифра больше второй")
else:
    print("Вторая и последняя цифры равны")