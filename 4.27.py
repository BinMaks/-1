num = int(input("Двузначное число: "))
first = num // 10
second = num % 10
square = num ** 2
sum_cubes = first ** 3 + second ** 3
if square == 4 * sum_cubes:
    print("Условие выполняется")
else:
    print("Условие не выполняется ")