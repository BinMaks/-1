t = float(input("Введите время t (минуты с начала часа): "))
t = t % 12
if 0 <= t < 3:
    print("Зеленый")
elif 3 <= t < 4:
    print("Желтый")
elif 4 <= t < 6:
    print("Красный")
else:
    print("Зеленый")