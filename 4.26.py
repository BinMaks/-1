num = int(input("Двузначное число: "))
first = num // 10
second = num % 10
if first > second:
    print("Первая цифра больше")
elif first < second:
    print("Вторая цифра больше")
else:
    print("Цифры одинаковы")

if first == second :
    print("Цифры одинакавы ")
else:
    print("Цифры разные")