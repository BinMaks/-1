num = int(input("Трехзначное число: "))
first = num // 100
last = num % 10
if first == last:
    print("Палиндром")
else:
    print("Не палиндром")