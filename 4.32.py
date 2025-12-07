num = int(input("Трехзначное число: "))
first = num // 100
second = (num // 10) % 10
last = num % 10
square = num ** 2
sum_cubes = first ** 3 + second ** 3 + last ** 3
if square == sum_cubes:
    print("Условие выполняется")
else:
    print("Условие не выполняется")